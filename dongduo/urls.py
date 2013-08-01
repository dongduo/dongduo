from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="Layout.html"), name="index"),
    # Examples:
    # url(r'^$', 'dongduo.views.home', name='home'),
    # url(r'^dongduo/', include('dongduo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     url(r'^api-auth',include('rest_framework.urls',namespace='rest_framework')),
     url(r'^blogs/', include('blogs.urls')),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
