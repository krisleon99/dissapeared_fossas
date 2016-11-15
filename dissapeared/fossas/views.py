import psycopg2
import json
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .models import Fossas
from .forms import Fossas_Form, Fossas_Update

@login_required(login_url='/manager/ingresar')
def list_fossas(request):
    agree = Fossas.objects.all()
    return render_to_response('fossas_list.html',{'items':agree}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('fossas.add_fossas')
def upload_fossas(request):
    if request.method=='POST':
        formulario = Fossas_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../address')
    else:
        formulario = Fossas_Form()
    return render_to_response('fossas_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('fossas.fossas')
def update_fossas(request, id_fossas):
    obj = get_object_or_404(Fossas, id=id_fossas)
    formulario = Fossas_Update(request.POST or None, instance=obj)
    if request.method == 'POST':

        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../')
    return render_to_response('fossas_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
def address_fossas(request):
    agree = Fossas.objects.all()
    if request.method=='POST':
        formulario = Fossas_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../')
    else:
        formulario = Fossas_Form()
    return render_to_response('fossas_address.html',{'items':agree, 'formulario':formulario}, context_instance=RequestContext(request))

"""
Mettodo para obtener desde ajax para mandar a llamar al upload de fosas
"""
def update_point_fosas(request):
    if request.is_ajax():
        try:
            conn = psycopg2.connect("dbname='fosas' user='postgres' host='localhost' password='postgres'")
            cur = conn.cursor()
            list_map = []
            points = request.POST.get('points', "None")
            some_lat = points.replace("[","").replace("]","")
            some_lat_lng = some_lat.split(",")
            lat = some_lat_lng[1]
            lng = some_lat_lng[0]
            print points
            print some_lat_lng
            print some_lat_lng[0]
            print some_lat_lng[1]
            if points not in "None":
                print "ok ok"
                fosa = Fossas.objects.latest('id')
                id_foss = int(fosa.id)
                print id_foss
                table = "spatial_fosa"
                cur.execute("insert into %s (fosa_id, the_geom) values(%s,ST_GeomFromText('POINT(%s %s)', 4326));" % (table, id_foss, lat, lng))
                conn.commit()
                print "Records created successfully";

        except psycopg2.DatabaseError, e:
            print "I am unable to connect to the database"
            print 'Error %s' % e
        finally:
            print "i dont undesrtand"
            if conn:
                conn.close()
        return HttpResponse(json.dumps(list_map), content_type='application/json' )
    else:
        return HttpResponse("Not ajax request")

@login_required(login_url='/manager/ingresar')
@permission_required('fossas.fossas')
def update_fossas_ubication(request, id_fossas):
    try:
        la_y = []
        conn = psycopg2.connect("dbname='fosas' user='postgres' host='localhost' password='postgres'")
        cur = conn.cursor()
        obj = get_object_or_404(Fossas, id=id_fossas)
        print obj
        table = "spatial_fosa"
        print id_fossas
        query = 'SELECT ST_AsText(the_geom) FROM spatial_fosa WHERE fosa_id = '+id_fossas+';'
        print query
        cur.execute(query)
        point_foss = cur.fetchone()
        print point_foss
        print point_foss[0]
        poff = point_foss[0].replace("POINT(","").replace(")","")
        print poff
        lng_lat = str(poff)
        print lng_lat
        for po_f in la_y:
            print po_f
            print "POINT(-99.165689 19.3536)"
        conn.commit()
        print "Records created successfully";

    except psycopg2.DatabaseError, e:
        print "I am unable to connect to the database"
        print 'Error %s' % e
    finally:
        print "i dont undesrtand"
        if conn:
            conn.close()
    return render_to_response('fossas_ubication_current.html',{'obj':obj, 'point_foss':str(lng_lat)}, context_instance=RequestContext(request))

def current_point_fosas(request):
    if request.is_ajax():
        try:
            print "entro a current point"
            conn = psycopg2.connect("dbname='fosas' user='postgres' host='localhost' password='postgres'")
            cur = conn.cursor()
            list_map = []
            points = request.POST.get('points', "None")
            some_lat = points.replace("[","").replace("]","")
            some_lat_lng = some_lat.split(",")
            id_foss = some_lat_lng[0]
            lat = some_lat_lng[1]
            lng = some_lat_lng[2]
            print some_lat_lng
            print lat
            print lng
            if points not in "None":
                print "updating"
                print id_foss
                table = "spatial_fosa"
                cur.execute("UPDATE %s SET the_geom = ST_GeomFromText('POINT(%s %s)', 4326) WHERE fosa_id=%s;" % (table,lng,lat,id_foss))
                conn.commit()
                print "Records created successfully";

        except psycopg2.DatabaseError, e:
            print "I am unable to connect to the database"
            print 'Error %s' % e
        finally:
            print "i dont undesrtand"
            if conn:
                conn.close()
        return HttpResponse(json.dumps(list_map), content_type='application/json' )
    else:
        return HttpResponse("Not ajax request")

@login_required(login_url='/manager/ingresar')
def list_fossas_location(request):
    try:
        fossas_id = []
        fossas_location = []
        arr_foss = []
        agree_fos = Fossas.objects.all()
        print agree_fos
        conn = psycopg2.connect("dbname='fosas' user='postgres' host='localhost' password='postgres'")
        cur = conn.cursor()
        table = "spatial_fosa"
        query = 'SELECT fosa_id, ST_AsText(the_geom) FROM spatial_fosa;'
        print query
        cur.execute(query)
        point_foss = cur.fetchall()
        print point_foss
        for fos in point_foss:
            print fos[0]
            print fos[1]
            for f_obj in agree_fos:
                if fos[0]==f_obj.id:
                    print "es igual el id"
                    poff = fos[1].replace("POINT(","").replace(")","")
                    poff_l = poff.split(" ")
                    print str(poff_l[0])
                    print poff_l[1]
                    print "poff_l[0]"
                    f_obj.lat = str(poff_l[0])
                    f_obj.lng = str(poff_l[1])
                    print f_obj.lat
            fossas_id.append(fos[0])
            fossas_location.append(fos[1])
            print "a wiwiw"
        arr_foss.append(fossas_id)
        arr_foss.append(fossas_location)
        print arr_foss
        conn.commit()
        print "Records created successfully";

    except psycopg2.DatabaseError, e:
        print "I am unable to connect to the database"
        print 'Error %s' % e
    finally:
        print "i dont undesrtand"
        if conn:
            conn.close()
    return render_to_response('fossas_location_list.html',{'agree_fos':agree_fos}, context_instance=RequestContext(request))