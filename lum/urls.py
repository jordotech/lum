from django.conf.urls import *

from django.contrib import admin
admin.autodiscover()
from django.conf import settings




from lum.views import home

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^(?i)admin/', include(admin.site.urls)),
]

if not settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns.append(url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

