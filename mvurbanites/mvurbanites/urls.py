from django.conf.urls import patterns, include, url
from django.contrib import admin

from mvurbanites.views import Home
from feature import urls as feature_urls
from blog import urls as blog_urls
from community import urls as community_urls
from impact import urls as impact_urls
from join import urls as join_urls
from support import urls as support_urls

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^feature/', include(feature_urls)),
    url(r'^blog/', include(blog_urls)),
    url(r'^community/', include(community_urls)),
    url(r'^impact/', include(impact_urls)),
    url(r'^join/', include(join_urls)),
    url(r'^support/', include(support_urls)),
    url(r'^admin/', include(admin.site.urls)),
)
