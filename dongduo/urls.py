from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# import apps
import users.urls

# enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="Layout.html"), name="index"),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^api/user_profiles/', include(users.urls)),
)

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
