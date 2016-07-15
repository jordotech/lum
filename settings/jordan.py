from .base import *
import os
DEBUG = True
SITE_ID = 2
def show_toolbar(request):
    return True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'lum.com']
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'settings.jordan.show_toolbar',
}

INSTALLED_APPS += (
    'debug_toolbar',
    'template_debug',
)

STATIC_ROOT = "/vagrant-data/lum/static/"
STATIC_URL ='/static/'
SECRET_KEY = os.environ["SECRET_KEY_LOCAL"]
DATABASES = {
    'default': {
        #'ENGINE': 'django_postgrespool',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'lum',
        'USER': 'deploy',             # Not used with sqlite3.
        #'USER': 'jordotech',             # Not used with sqlite3.
        'PASSWORD': 'happy',         # Not used with sqlite3.
        #'PASSWORD': 'Login4040',         # Not used with sqlite3.
        'HOST': '',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',             # Set to empty string for default. Not used with sqlite3.
    }
}