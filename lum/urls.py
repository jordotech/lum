from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()
from django.conf import settings
urlpatterns = patterns('',
    url(r'^$', 'lum.views.home', name='home'),
    (r'^(?i)admin/',  include(admin.site.urls)), # admin site
)

if not settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))