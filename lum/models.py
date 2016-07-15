from django.db import models

from django.db.models.signals import pre_delete, post_save
#from django.contrib.localflavor.us.models import USPostalCodeField, USStateField, PhoneNumberField
from django.conf import settings

import json
import logging





class Lab(models.Model):
    name = models.CharField('Name', max_length=200, blank=True, null=True)
    address = models.CharField('Address', max_length=200, blank=True, null=True)
    organization = models.CharField('Organization', max_length=200, blank=True, null=True)
    department = models.CharField('Department', max_length=200, blank=True, null=True)
    city = models.CharField('City', max_length=150, blank=True, null=True)
    province = models.CharField('Province', max_length=100, blank=True)
    postal_code = models.CharField('Postal Code', max_length=11, blank=True, null=True)
    country = models.CharField('Country', max_length=30, null=True, blank=True)
    phone = models.CharField('Phone', max_length=30, blank=True, null=True)
    def classname(self):
        classname = self.__class__.__name__
        return classname
    class Meta:
        verbose_name = 'Lab'
        verbose_name_plural = 'Labs'
    def __unicode__(self):
        return "%s" % self.organization

class Author(models.Model):
    name = models.CharField('Name', max_length=200)
    labs = models.ManyToManyField(Lab, related_name="author_set", verbose_name="labs", blank=True,)

    def classname(self):
        classname = self.__class__.__name__
        return classname
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    def __unicode__(self):
        return self.name
#from taggit.managers import TaggableManager
from taggit_autosuggest.managers import TaggableManager
#from taggit.managers import TaggableManager
from taggit.models import TaggedItemBase

class CISTags(TaggedItemBase):
    content_object = models.ForeignKey('Publication')

    def classname(self):
        classname = self.__class__.__name__
        return classname

    class Meta:
        verbose_name = 'CIS Keyword Tag'
        verbose_name_plural = 'CIS Keyword Tags'

    def __unicode__(self):
        return "CIS Keyword - %s" % self.pk

class Publication(models.Model):
    pmid = models.CharField("PMID", max_length=255)
    title = models.CharField("Title", max_length=500, blank=True, null=True,)
    abstract = models.TextField('Abstract', blank=True, null=True)
    doi = models.CharField("DOI", blank=True, null=True, help_text="Digital object identifier", max_length=255)
    authors = models.ManyToManyField(Author, related_name="author_set", verbose_name="authors")
    labs = models.ManyToManyField(Lab, related_name="pub_set", verbose_name="labs", blank=True, )
    cis_keywords = TaggableManager("CIS Keywords", through=CISTags, help_text="Search terms used to find this publication on PubSearch")
    def classname(self):
        classname = self.__class__.__name__
        return classname
    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
    def __unicode__(self):
        return "Publication - %s" % self.doi