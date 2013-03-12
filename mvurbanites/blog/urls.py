from django.conf.urls import patterns, url

from blog.views import BlogList, BlogDetail

urlpatterns = patterns('blog',
    url(r'^$', BlogList.as_view(), name='blog'),
    url(r'^(?P<slug>[-\w]+)/$', BlogDetail.as_view(), name='blog_detail'),
)
