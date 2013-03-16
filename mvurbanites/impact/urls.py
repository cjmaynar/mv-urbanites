from django.conf.urls import patterns, url

from impact.views import *


urlpatterns = patterns('impact',
    url(r'^$', ImpactView.as_view(), name='impact'),
)
