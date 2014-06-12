try:
    from django.conf.urls import patterns, url, include
except ImportError:  # Django<=1.4
    from django.conf.urls.defaults import patterns, url, include

from django.contrib import admin

import nexus

admin.autodiscover()
nexus.autodiscover()

urlpatterns = patterns('',
    url(r'', include(nexus.site.urls)),
)
