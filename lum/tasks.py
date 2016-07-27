from __future__ import absolute_import
from celery import task, shared_task
from celery import Celery
from django.conf import settings
#app = Celery('lum.tasks', broker=settings.BROKER_URL)
from Bio import Entrez

@task(queue="lum", name="scrape_pubmed")
def scrape_pubmed(publication, query):
    pass
    '''
    Entrez.email = "jordotech@gmail.com"
    handle = Entrez.efetch(db="pubmed", id=publication.pmid, retmode="xml")
    data = Entrez.read(handle)
    handle.close()
    authors = []
    article = data[0]['MedlineCitation']['Article']
    try:
        authors = article['AuthorList']
    except:
        pass
    else:
        publication.update_authors(authors)

    abstract = ''
    try:
        abstract = article['Abstract']['AbstractText']
    except:
        pass
    else:
        publication.abstract = abstract
        publication.title = article['ArticleTitle']

    if query:
        publication.cis_keywords.add(unicode(query))

        publication.save()
    '''
