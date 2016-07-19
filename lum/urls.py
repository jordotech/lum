from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()
from django.conf import settings

from django.conf.urls.static import static


from lum.views import home, search

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^search/$', search, name='home'),
    url(r'^(?i)admin/', include(admin.site.urls)),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url('^', include('django.contrib.auth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if not settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns.append(url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

