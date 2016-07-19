from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()
from django.conf import settings

from django.conf.urls.static import static


from lum.views import home, search, saved_searches

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^search/$', search, name='home'),

    url(r'^saved-searches/(?P<pk>\S+?)/$', saved_searches, name='saved_search'),
    url(r'^saved-searches/$', saved_searches, name='saved_search_list'),
    url(r'^(?i)admin/', include(admin.site.urls)),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url('^', include('django.contrib.auth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if not settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns.append(url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

