from django.conf.urls import patterns, include, url

from .views import AccountView

urlpatterns = patterns('',
    url(r'^$', AccountView.as_view(), name='account'),
)

