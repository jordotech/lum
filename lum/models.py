from django.db import models
from django.contrib.auth.models import User
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
    country = models.CharField('Country', max_length=2, null=True, blank=True)
    phone = models.CharField('Phone', max_length=30, blank=True, null=True)
    def classname(self):
        classname = self.__class__.__name__
        return classname
    class Meta:
        verbose_name = 'Lab'
        verbose_name_plural = 'Labs'
    def __unicode__(self):
        return self.name

class Author(models.Model):
    name = models.CharField('Name', max_length=200)
    labs = models.ManyToManyField(Lab, related_name="labs_set", verbose_name="labs", null=True, blank=True,)

    def classname(self):
        classname = self.__class__.__name__
        return classname
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    def __unicode__(self):
        return self.name

class Publication(models.Model):
    pmid = models.CharField("PMID", max_length=255)
    abstract = models.TextField('Abstract', blank=True, null=True)
    doi = models.CharField("DOI", blank=True, null=True, help_text="Digital object identifier", max_length=255)
    authors = models.ManyToManyField(Author, related_name="author_set", verbose_name="authors")
    def classname(self):
        classname = self.__class__.__name__
        return classname
    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
    def __unicode__(self):
        return "Publication - %s" % self.doi