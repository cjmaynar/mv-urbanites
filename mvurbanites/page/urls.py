from django.conf.urls import patterns, include, url

from .views import PageView, SearchView, SectionView

urlpatterns = patterns('',
    url(r'^$', PageView.as_view(), name='home'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^(?P<slug>[-\w]+)/$', SectionView.as_view(), name='section'),
    url(r'^(?P<section>[-\w]+)/(?P<slug>[-\w]+)/$', PageView.as_view(), name='page'),
)
