from django.conf.urls import patterns, include, url

from .views import *

urlpatterns = patterns('account',
    url(r'^$', AccountView.as_view(), name='account'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^join/$', JoinView.as_view(), name='join'),
)

