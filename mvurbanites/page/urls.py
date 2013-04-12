from django.conf.urls import patterns, include, url

from .views import PageView, SearchView

urlpatterns = patterns('',
    url(r'^$', PageView.as_view(), name='home'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'(?P<slug>[-\w]+)/$', PageView.as_view(), name='page'),
)
