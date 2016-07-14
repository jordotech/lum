from .base import *
import os
DEBUG = False
SITE_ID = 2

INSTALLED_APPS += (
    'debug_toolbar',
    'template_debug',
)
STATIC_ROOT = "/webapps/lum/static-collect/"

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