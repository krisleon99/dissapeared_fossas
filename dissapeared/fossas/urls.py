# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import patterns, include, url

js_info_dict = {
    'packages': ('dissapeared.fossas',),
}

urlpatterns = patterns('dissapeared.fossas.views',

                       url(r'^$', 'list_fossas', name='list_fossas'),

                       url(r'^upload/$', 'upload_fossas', name='upload_fossas'),

                       url(r'^update/(?P<id_fossas>\d+)$', 'update_fossas', name='update_fossas'),

                       url(r'^address/$', 'address_fossas', name='address_fossas'),
 
                       url(r'^address/update_point_fosas/$', 'update_point_fosas', name='update_point_fosas'),

                       url(r'^update_ubication/(?P<id_fossas>\d+)$', 'update_fossas_ubication', name='update_fossas_ubication'),

                       url(r'^address/current_point_fosas/$', 'current_point_fosas', name='current_point_fosas'),

                       url(r'^locations/$', 'list_fossas_location', name='list_fossas_location'),

                       ) 
