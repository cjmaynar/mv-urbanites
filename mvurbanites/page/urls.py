from django.conf.urls import patterns, include, url

from page.views import PageDetail

urlpatterns = patterns('',
    url(r'^(?P<slug>[\w]+)/$', PageDetail.as_view(), name='page'),
    url(r'^(?P<category>[\w]+)/(?P<slug>[-\w]+)/', PageDetail.as_view(), name='page'),
)
