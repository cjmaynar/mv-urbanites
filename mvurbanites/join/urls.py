from django.conf.urls import patterns, url

from join.views import *


urlpatterns = patterns('join',
    url(r'^$', JoinView.as_view(), name='join'),
)
