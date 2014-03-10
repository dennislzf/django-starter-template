from django.conf.urls import patterns, url, include

from django.contrib import admin
from django.conf import settings

admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^admin/', include(admin.site.urls)),
	 url(r'^$', 'veritaslaw.views.home', name='home'),
    # Examples:
    # url(r'^$', 'veritaslaw.views.home', name='home'),
    # url(r'^veritaslaw/', include('veritaslaw.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
