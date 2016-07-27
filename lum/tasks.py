from __future__ import absolute_import

from celery import shared_task, task


from Bio import Entrez
import logging
logger = logging.getLogger('lum')

@task(queue="lum", name="scrape_pubmed")
def scrape_pubmed(publication, query):
    logger.debug(type(publication))
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