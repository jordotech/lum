from django.db import models
from django.utils import timezone


class Url(models.Model):
    url = models.CharField('Name', max_length=250)
    active = models.BooleanField("Active", default=True)
    stop_notifying = models.BooleanField("Stop Notifying", default=False)
    created = models.DateTimeField(auto_now_add=True)
    notified = models.DateTimeField("Notified on", blank=True, null=True,)
    modified = models.DateTimeField(auto_now=True)

    def classname(self):
        classname = self.__class__.__name__
        return classname

    class Meta:
        verbose_name = 'Url Pinger'
        verbose_name_plural = 'Url Pingers'

    def __unicode__(self):
        return "%s" % self.url
