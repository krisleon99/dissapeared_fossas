import psycopg2
import json
from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse, HttpResponseRedirect, Http404

from .models import Missing, Place_Missing, Origin, Physical_Description
from .forms import Missing_Form, Missing_Update, Origin_Form, Origin_Update 
from .forms import Place_Form, Place_Update, Physical_Description_Form, Physical_Description_Update

@login_required(login_url='/manager/ingresar')
def list_missing(request):
    agree = Missing.objects.all()
    return render_to_response('missing_list.html',{'items':agree}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('missing.add_missing')
def upload_missing(request):
    if request.method=='POST':
        formulario = Missing_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            mis = Missing.objects.latest('id')
            return HttpResponseRedirect('../detail/'+str(mis.id))
    else:
        formulario = Missing_Form()
    return render_to_response('missing_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('missing.change_missing')
def update_missing(request, id_missing):
    obj = get_object_or_404(Missing, id=id_missing)
    formulario = Missing_Update(request.POST or None, instance=obj)
    if request.method == 'POST':

        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../')
    return render_to_response('missing_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
def detail_missing(request, id_missing):
    miss = get_object_or_404(Missing, id=id_missing)
    origi_m = get_object_or_404(Origin,missing_id=id_missing)
    place = get_object_or_404(Place_Missing,missing_id=id_missing)
    physic = get_object_or_404(Physical_Description,missing_id=id_missing)

    return render_to_response('missing_ detail.html',{'miss':miss, 'origi_m':origi_m, 'place':place, 'physic':physic}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('missing.add_missing')
def upload_origin(request):
    if request.method=='POST':
        formulario = Origin_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../')
    else:
        formulario = Origin_Form()
    return render_to_response('origin_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('missing.add_missing')
def upload_place(request):
    if request.method=='POST':
        formulario = Place_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../address_miss')
    else:
        formulario = Place_Form()
    return render_to_response('place_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('missing.add_missing')
def upload_Physical_Description(request):
    if request.method=='POST':
        formulario = Physical_Description_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../')
    else:
        formulario = Physical_Description_Form()
    return render_to_response('physical_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
def address_missing(request):
    agree = Missing.objects.all()
    if request.method=='POST':
        formulario = Missing_Form(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../')
    else:
        formulario = Missing_Form()
    return render_to_response('missing_address.html',{'items':agree, 'formulario':formulario}, context_instance=RequestContext(request))


def update_point_missing(request):
    if request.is_ajax():
        try:
            print "vamos bien"
            conn = psycopg2.connect("dbname='fosas' user='postgres' host='localhost' password='postgres'")
            cur = conn.cursor()
            list_map = []
            print "point"
            points = request.POST.get('points', "None")
            print points
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
                fosa = Missing.objects.latest('id')
                id_foss = int(fosa.id)
                print id_foss
                table = "spatial_missing"
                cur.execute("insert into %s (missing_id, the_geom) values(%s,ST_GeomFromText('POINT(%s %s)', 4326));" % (table, id_foss, lat, lng))
                conn.commit()
                print "Records created successfully";

        except psycopg2.DatabaseError, e:
            print "I am unable to connect to the database"
            print 'Error %s' % e
        finally:
            if conn:
                conn.close()
        return HttpResponse(json.dumps(list_map), content_type='application/json' )
    else:
        return HttpResponse("Not ajax request")

@login_required(login_url='/manager/ingresar')
def list_missing_location(request):
    try:
        fossas_id = []
        fossas_location = []
        arr_foss = []
        agree_fos = Missing.objects.all()
        print agree_fos
        conn = psycopg2.connect("dbname='fosas' user='postgres' host='localhost' password='postgres'")
        cur = conn.cursor()
        table = "spatial_missing"
        query = 'SELECT missing_id, ST_AsText(the_geom) FROM spatial_missing;'
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
            print "ejole"
        arr_foss.append(fossas_id)
        arr_foss.append(fossas_location)
        print arr_foss
        conn.commit()
        print "Records created successfully";

    except psycopg2.DatabaseError, e:
        print "I am unable to connect to the database"
        print 'Error %s' % e
    finally:
        if conn:
            conn.close()
    return render_to_response('missing_location_list.html',{'agree_fos':agree_fos}, context_instance=RequestContext(request))