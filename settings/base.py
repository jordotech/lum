from __future__ import absolute_import
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
import djcelery
from datetime import timedelta

SECRET_KEY = 'g+)@fwqh$60!^hu^p%0xsm=5e50vg&+f!dkz8fbbm*1_t$yop3'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'settings',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'taggit',
    #'taggit_templatetags',
    'taggit_autosuggest',
    'django_extensions',
    'celery',
    'flower',
    'lum.apps.LumAppConfig',
    'pinger',

)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],

        },
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
    },
]
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lum.urls'

WSGI_APPLICATION = 'lum.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
from .log_settings import *

CELERY_IMPORTS = ("lum.tasks",)
CELERY_TIMEZONE = 'UTC'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['pickle', 'json']
CELERYD_POOL_RESTARTS = True
BROKER_URL = 'redis://localhost:6379/0' #redis

CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

CELERYBEAT_SCHEDULE = {
    'celerybeat_healthcheck': {
        'task': 'lum.tasks.celerybeat_healthcheck',
        'schedule': timedelta(seconds=5),
    },
    'pinger': {
        'task': 'pinger.tasks.pinger',
        'schedule': timedelta(seconds=10),
    },

}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

EMAIL_HOST_USER = 'admin@cg-dev.com'
EMAIL_HOST_PASSWORD = 'Login4040'
EMAIL_USE_TLS = True