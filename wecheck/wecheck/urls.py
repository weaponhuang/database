from django.conf.urls import patterns, include, url
from wecheck import settings
from v_site import urls

import xadmin
xadmin.autodiscover()

# from xadmin.plugins import xversion
# xversion.registe_models()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wecheck.views.home', name='home'),
    # url(r'^wecheck/', include('wecheck.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'xadmin/', include(xadmin.site.urls)),
    url(r'', include('v_site.urls')),
)
