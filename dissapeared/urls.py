# -*- coding: utf-8 -*-
#########################################################################
#
#
#########################################################################

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

js_info_dict = {
    'packages': ('dissapeared',),
}

urlpatterns = patterns('',

                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       url(r'^admin/', include(admin.site.urls)),

                       # url(r'^avatar/', include('avatar.urls')),

                       url(r'^$', include('dissapeared.manager.urls')),
                       
                       url(r'^manager/', include('dissapeared.manager.urls')),

                       url(r'^fossas/', include('dissapeared.fossas.urls')),

                       url(r'^missing/', include('dissapeared.missing.urls')),

                       # Accounts
                       url(r'^accounts/', include('dissapeared.accounts.urls')),

                       )

# Serve static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
