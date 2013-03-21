from django.conf.urls import patterns, include, url
from django.contrib import admin

from mvurbanites.views import Home
from feature import urls as feature_urls
from blog import urls as blog_urls
from page import urls as page_urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^feature/', include(feature_urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(page_urls)),
)
