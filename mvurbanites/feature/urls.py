from django.conf.urls import patterns, url

from feature.views import FeatureList, FeatureDetail

urlpatterns = patterns('feature',
    url(r'^$', FeatureList.as_view(), name='feature'),
    url(r'^(?P<slug>[-\w]+)/$', FeatureDetail.as_view(), name='feature_detail'),
)
