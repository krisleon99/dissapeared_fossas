# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import patterns, include, url

js_info_dict = {
    'packages': ('dissapeared.accounts',),
}

urlpatterns = patterns('dissapeared.accounts.views',

                       url(r'^login/$', 'denied_access', name='denied_access'),

                       )
