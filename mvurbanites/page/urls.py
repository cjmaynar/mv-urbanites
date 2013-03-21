from django.conf.urls import patterns, include, url

from .views import PageDetail, PageLanding

urlpatterns = patterns('',
    url(r'^(?P<slug>[\w]+)/$', PageLanding.as_view(), name='section'),
    url(r'^(?P<category>[\w]+)/(?P<slug>[-\w]+)/', PageDetail.as_view(), name='page'),
)
