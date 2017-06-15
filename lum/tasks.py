from __future__ import absolute_import

from celery import shared_task, task


from Bio import Entrez
import logging
logger = logging.getLogger('lum')


import logging

@task()
def celerybeat_healthcheck():
    print 'foo'
    logger.debug('running healthcheck task...')
    return True

'''


@task(queue="lum", name="scrape_pubmed")
def scrape_pubmed(publication, query):
    Entrez.email = "jordotech@gmail.com"
    handle = Entrez.efetch(db="pubmed", id=publication.pmid, retmode="xml")
    data = Entrez.read(handle)
    handle.close()
    authors = []
    article = data[0]['MedlineCitation']['Article']
    eid_type = None
    try:
        eid_type = article['ELocationID'][0].attributes['EIdType']
        doi = str(article['ELocationID'][0])
    except: pass
    else:
        if eid_type == 'doi':
            publication.doi = doi
    print data[0]['MedlineCitation']
    try:
        authors = article['AuthorList']
    except:
        pass
    else:
        publication.update_authors(authors)

    abstract = ''
    try:
        abstract = article['Abstract']['AbstractText']
        publication.abstract = abstract

    except:
        pass
    publication.title = article['ArticleTitle']

    if query:
        publication.cis_keywords.add(unicode(query))
    publication.save()

'''