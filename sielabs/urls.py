from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'consultas.views.home'),
    url(r'^nosotros/$', 'consultas.views.nosotros'),
    url(r'^servicios/$', 'consultas.views.servicios'),
    url(r'^cursos/$', 'consultas.views.temascursos'),
    url(r'^contactos/$', 'consultas.views.new_contacto'),
    # url(r'^sielabs/', include('sielabs.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
