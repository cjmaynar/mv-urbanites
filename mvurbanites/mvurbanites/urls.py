from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from mvurbanites.views import Home
import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^feature/', include('feature.urls')),
    url(r'^', include('page.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
