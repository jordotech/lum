from __future__ import absolute_import

from celery import shared_task, task


import logging
logger = logging.getLogger('lum')

@task()
def pinger():


    return True