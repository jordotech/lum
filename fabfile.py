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

def email():
    from django.core.mail import send_mail

    send_mail(
        'Subject here',
        'Here is the message.',
        'admin@cg-dev.com',
        ['jordotech@gmail.com'],
        fail_silently=False,
    )
'''
from lum.tasks import scrape_pubmed
def test(pmid):
    p = Publication.objects.get(pmid=pmid)
    scrape_pubmed(p, None)
'''
