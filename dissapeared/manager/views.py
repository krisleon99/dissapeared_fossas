from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

from dissapeared.fossas.models import Fossas
from .forms import User_Basic_Update, User_Change_Password
from django.contrib.auth.models import User
# from django.contrib.auth.views import password_change

@login_required(login_url='/manager/ingresar')
def agreement_and_proposal(request):
    pro = Fossas.objects.all()
    return render_to_response('index.html',{'pro':pro}, context_instance=RequestContext(request))

def home_page(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/manager/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    here = request.GET.get('next', '')
                    return HttpResponseRedirect('../..'+here)
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

@permission_required('is_staff')
def nuevo_usuario(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/manager/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    here = request.GET.get('next', '')
                    return HttpResponseRedirect('../..'+here)
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    return render_to_response('privado.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='/manager/ingresar')
def user_list(request):
    users = User.objects.all()
    print users
    return render_to_response('user_list.html',{'items':users}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
def user_detail(request, id_user):
    user = get_object_or_404(User, pk=id_user)
    return render_to_response('user_detail.html',{'us':user}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
@permission_required('manager.change_user')
def user_update(request, id_user):
    id_user_loged = request.user.id
    print id_user_loged
    print id_user
    #if int(id_user) == int(id_user_loged):
    obj = get_object_or_404(User, id=id_user)
    formulario = UserChangeForm(request.POST or None, instance=obj)
    if request.method == 'POST':

        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../detail/'+ id_user)
    #else:
        #return HttpResponseRedirect('/')
    return render_to_response('user_form.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/manager/ingresar')
def user_update_basic(request, id_user):
    id_user_loged = request.user.id
    print id_user_loged
    print id_user
    #if int(id_user) == int(id_user_loged):
    obj = get_object_or_404(User, id=id_user)
    formulario = User_Basic_Update(request.POST or None, instance=obj)
    # change_password = password_change(user=request.user, data=request.POST)#User_Change_Password(request.POST or None, instance=obj)
    if request.method == 'POST':

        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('../detail/'+ id_user)

    #if change_password.is_valid():
     #       change_password.save()
      #      update_session_auth_hash(request, change_password.user)
    #else:
        #return HttpResponseRedirect('/')
    return render_to_response('user_basic_form.html',{'formulario':formulario, 'id_user':id_user}, context_instance=RequestContext(request))#, 'change_password': change_password}, context_instance=RequestContext(request))


@login_required(login_url='/manager/ingresar')
def change_password(request):
    id_user_loged = request.user.id
    print id_user_loged
    #if int(id_user) == int(id_user_loged):
    obj = get_object_or_404(User, id=id_user_loged)
    formulario = User_Change_Password(request.POST or None)
    if request.method == 'POST':

        if formulario.is_valid():
            password_old = request.POST['old_password'];
            password_new = request.POST['password'];
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(password_new)
            u.save()

            # formulario.set_password(password_new)
            # formulario.save()
            return HttpResponseRedirect('../detail/'+ str(request.user.id))
    #else:
        #return HttpResponseRedirect('/')
    return render_to_response('password_change_form.html',{'formulario':formulario}, context_instance=RequestContext(request))