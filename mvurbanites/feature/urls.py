from django.conf.urls import patterns, url

from feature.views import FeatureList, FeatureDetail

urlpatterns = patterns('feature',
    url(r'^$', FeatureList.as_view(), name='feature'),
    url(r'^(?P<pk>\d+)/$', FeatureDetail.as_view(), name='feature_detail'),
)
