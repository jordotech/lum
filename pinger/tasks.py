from __future__ import absolute_import

from celery import shared_task, task
from .models import Url

import logging
logger = logging.getLogger('lum')

def email():
    from django.core.mail import send_mail

    send_mail(
        '%s is down' % (url),
        'Here is the message.',
        'admin@cg-dev.com',
        ['jordotech@gmail.com'],
        fail_silently=False,
    )
import requests
@task()
def pinger():
    logger.debug('in ping...')
    for url in Url.objects.filter(active=True, stop_notifying=False):
        response = requests.get(url.url)
        logger.debug(response.status_code)
    return True