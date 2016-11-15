# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import patterns, include, url

js_info_dict = {
    'packages': ('dissapeared.missing',),
}

urlpatterns = patterns('dissapeared.missing.views',

                       url(r'^$', 'list_missing', name='list_missing'),

                       url(r'^upload/$', 'upload_missing', name='upload_missing'),

                       url(r'^update/(?P<id_missing>\d+)$', 'update_missing', name='update_missing'),

                       url(r'^detail/(?P<id_missing>\d+)$', 'detail_missing', name='detail_missing'),

                       url(r'^origin/$', 'upload_origin', name='upload_origin'),

                       url(r'^place/$', 'upload_place', name='upload_place'),

                       url(r'^physical/$', 'upload_Physical_Description', name='upload_Physical_Description'),

                       url(r'^address_miss/$', 'address_missing', name='address_missing'),

                       url(r'^address_miss/update_point_missing/$', 'update_point_missing', name='update_point_missing'),

                       url(r'^locations_miss/$', 'list_missing_location', name='list_missing_location'),

                       )
