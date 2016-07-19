from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()
from django.conf import settings

from django.conf.urls.static import static


from lum.views import home, search, saved_searches, save_user_query, delete_user_query, save_pmid_to_query

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^search/$', search, name='home'),
    url(r'^saved-searches/(?P<pk>\S+?)/$', saved_searches, name='saved_search'),
    url(r'^saved-searches/$', saved_searches, name='saved_search_list'),
    url(r'^save-user-query/(?P<query>.*)/$', save_user_query, name='save_user_query'),
    url(r'^save-pmid-to-query/(?P<pk>\S+?)/(?P<pmid>\S+?)/$', save_pmid_to_query, name='save_pmid_to_query'),
    url(r'^delete-user-query/(?P<pk>\S+?)/$', delete_user_query, name='delete_user_query'),
    url(r'^(?i)admin/', include(admin.site.urls)),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url('^', include('django.contrib.auth.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if not settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns.append(url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

