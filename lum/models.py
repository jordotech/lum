from django.db import models
import datetime
from django.db.models.signals import pre_delete, post_save
#from django.contrib.localflavor.us.models import USPostalCodeField, USStateField, PhoneNumberField
from django.conf import settings

import json
import logging

from taggit_autosuggest.managers import TaggableManager
from taggit.models import TaggedItemBase
from django.contrib.auth.models import User

from django.core.exceptions import FieldError
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
    first_name = models.CharField('First Name', max_length=200)
    last_name = models.CharField('Last Name', max_length=200)
    initials = models.CharField('Initials', max_length=20)
    labs = models.ManyToManyField(Lab, related_name="author_set", verbose_name="labs", blank=True, null=True,)
    @property
    def full_name(self):
        return '%s, %s' % (self.last_name, self.first_name)
    def classname(self):
        classname = self.__class__.__name__
        return classname
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    def __unicode__(self):
        return self.full_name

#class AuthorIdentifier(models.Model):
    #identifier = models.CharField('Identifier', max_length=200, help_text="see https://www.nlm.nih.gov/bsd/mms/medlineelements.html#auid")
    #author = models.ForeignKey(Author)

class AuthorAffiliation(models.Model):
    affiliation = models.TextField('Affiliation', blank=True, null=True)
    identifier = models.CharField('Identifier', max_length=200, help_text="see https://www.nlm.nih.gov/bsd/mms/medlineelements.html#auid")
    author = models.ForeignKey(Author)

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
from django.utils import timezone
from metapub import PubMedFetcher
from Bio import Entrez
import logging
logger = logging.getLogger('lum')
class Publication(models.Model):
    created = models.DateTimeField(editable=False, default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())
    pmid = models.CharField("PMID", max_length=255)
    title = models.CharField("Title", max_length=500, blank=True, null=True,)
    abstract = models.TextField('Abstract', blank=True, null=True)
    doi = models.CharField("DOI", blank=True, null=True, help_text="Digital object identifier", max_length=255)
    authors = models.ManyToManyField(Author, related_name="author_set", verbose_name="authors")
    labs = models.ManyToManyField(Lab, related_name="pub_set", verbose_name="labs", blank=True, )
    cis_keywords = TaggableManager("Queries used", through=CISTags, help_text="Search terms used to find this publication on PubMed")
    def update_authors(self, authors):
        for row in authors:
            last_name = row['LastName']
            initials = row['Initials']
            first_name = row['ForeName']
            author = Author.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                initials=initials,
            )[0]
            for aff in row['AffiliationInfo']:
                author_aff = AuthorAffiliation.objects.get_or_create(
                    affiliation=aff['Affiliation'],
                    author=author,
                )[0]

    def self_update(self, query=None):
        Entrez.email = "jordotech@gmail.com"
        handle = Entrez.efetch(db="pubmed", id=self.pmid, retmode="xml")
        data = Entrez.read(handle)
        handle.close()
        authors = []
        article = data[0]['MedlineCitation']['Article']
        try: authors = article['AuthorList']
        except: pass
        else:
            self.update_authors(authors)

        abstract = ''
        try: abstract = article['Abstract']['AbstractText']
        except: pass
        else:
            self.abstract = abstract
        self.title = article['ArticleTitle']

        if query:
            self.cis_keywords.add(unicode(query))

        self.save()
    def classname(self):
        classname = self.__class__.__name__
        return classname
    class Meta:
        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'
    def __unicode__(self):
        return "Publication - %s" % self.doi

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Publication, self).save(*args, **kwargs)

'''
class UserPmid(models.Model):
    publication = models.ForeignKey(Publication)
    user = models.ForeignKey(User)
    staff_notes = models.TextField('Staff Notes', blank=True, null=True)
'''


class SearchStash(models.Model):
    created = models.DateTimeField(editable=False, default=timezone.now())
    modified = models.DateTimeField(default=timezone.now())
    search_used = models.CharField("Search Used", max_length=255)
    user = models.ForeignKey(User)
    pmids = models.ManyToManyField(Publication)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(SearchStash, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return "/saved-searches/%s/" % str(self.id)