# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib import admin
from django.contrib.auth.views import password_change_done

js_info_dict = {
    'packages': ('dissapeared.manager',),
}

urlpatterns = patterns('dissapeared.manager.views',

                       url(r'^$', 'home_page', name='home_page'),

                       url(r'^home/$', 'agreement_and_proposal', name='agreement_and_proposal'),

                       url(r'^usuario/nuevo$','nuevo_usuario'),

                       url(r'^ingresar/$','ingresar'),

                       url(r'^privado/$','privado'),

                       url(r'^cerrar/$', 'cerrar'),

                       url(r'^usuario/list$','user_list'),

                       url(r'^usuario/detail/(?P<id_user>\d+)$','user_detail'),

                       url(r'^usuario/update/(?P<id_user>\d+)$','user_update'),

                       url(r'^usuario/update_basic/(?P<id_user>\d+)$','user_update_basic'),

                       url(r'^usuario/change_password/$','change_password'),

                       # url(r'^change/$', 'avatar_change'),

                       )
#urlpatterns += patterns('',
 # (r'^password_change_done/$', 'django.contrib.auth.views.password_change_done','password_change_done'),
#)