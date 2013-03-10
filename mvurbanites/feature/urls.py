from django.conf.urls import patterns, url

from feature.views import Feature

urlpatterns = patterns('feature',
    url(r'^$', Feature.as_view(), name='feature'),
)
