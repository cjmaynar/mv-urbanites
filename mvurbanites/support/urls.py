from django.conf.urls import patterns, url

from support.views import *


urlpatterns = patterns('support',
    url(r'^$', SupportView.as_view(), name='support'),
)
