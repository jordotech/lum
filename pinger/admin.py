# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Url


class UrlAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'url',
        'active',
        'stop_notifying',
        'created',
        'notified',
        'modified',
    )
    list_filter = (
        'active',
        'stop_notifying',
        'created',
        'notified',
        'modified',
    )
    list_editable = ('url', 'active', 'stop_notifying',)
admin.site.register(Url, UrlAdmin)