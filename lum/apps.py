# lum/apps.py

from django.apps import AppConfig


class LumAppConfig(AppConfig):
    name = 'lum'
    verbose_name = 'Luminex'

    def ready(self):
        pass

