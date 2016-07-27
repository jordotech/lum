import django

django.setup()
from lum.models import *
from metapub import PubMedFetcher


def clear():
    Lab.objects.all().delete()
    Author.objects.all().delete()
    Publication.objects.all().delete()
    SearchStash.objects.all().delete()
    AuthorAffiliation.objects.all().delete()


def psearch(pmid):
    fetch = PubMedFetcher()
    ret = fetch.article_by_pmid(pmid)
    print ret.to_dict()
from lum.tasks import scrape_pubmed
def test(pmid):
    p = Publication.objects.get(pmid=pmid)
    scrape_pubmed(p, None)