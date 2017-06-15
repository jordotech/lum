from __future__ import absolute_import, unicode_literals
import os
from django.conf import settings
from celery import Celery
from unipath import Path
import dotenv
# set the default Django settings module for the 'celery' program.
dotenv.read_dotenv(Path(__file__).ancestor(2).child('.env'))
app = Celery('lum', broker=settings.BROKER_URL)

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object('django.conf:settings', namespace='CELERYBEAT')
app.conf.beat_schedule = settings.CELERYBEAT_SCHEDULE

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
