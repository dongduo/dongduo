from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'(?P<pk>\d+)/$',
        views.UserProfileDetail.as_view(),
        name='user_profile_detail'),
)
