from __future__ import absolute_import, unicode_literals
default_app_config = 'lum.apps.LumAppConfig'


from .celeryconfig import app as celery_app

__all__ = ['celery_app']