from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('book_catalog.views',
    # Main
    url(r'^$', 'index'),
    url(r'^p/([\w-]+)/$', 'page'),
    #url(r'^contact$', 'contact'),

    url(r'^catalog$', 'catalog'),
    # Series & Books
    url(r'^catalog/([\w-]+)/$', 'series'), # breaks when trailing slash is removed...
    url(r'^catalog/([\w-]+)/([\w-]+)$', 'book'),

    url(r'^contact/', include("contact_form.urls", namespace="contact_form")),

    url(r'^admin/', include(admin.site.urls)),

    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^m/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
