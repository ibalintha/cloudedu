from django.conf.urls import patterns, include, url
from system import site
import system
system.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cloudedu.views.index', name='index'),
    url(r'^essential/', include('essential.urls')),
    # url(r'^cloudedu/', include('cloudedu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^system/', include(site.urls)),
)
