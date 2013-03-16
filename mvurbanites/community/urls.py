from django.conf.urls import patterns, url

from community.views import *

urlpatterns = patterns('community',
    url(r'^$', CommunityView.as_view(), name='community'),
)
