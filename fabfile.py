import django

django.setup()
from lum.models import *
from metapub import PubMedFetcher


def clear():
    Lab.objects.all().delete()
    Author.objects.all().delete()
    Publication.objects.all().delete()
    SearchStash.objects.all().delete()

def psearch(pmid):
    fetch = PubMedFetcher()
    ret = fetch.article_by_pmid(pmid)
    print ret.to_dict()

    test = {'pii': 'jogh-05-020417',
            'publication_types': {'D016428': 'Journal Article', 'D013485': "Research Support, Non-U.S. Gov't"},
            'book_language': None,
            'abstract': u'BACKGROUND: Respiratory syncytial virus (RSV) is the most important cause of acute respiratory tract infection (ARTI) related morbidity and mortality worldwide. However, the disease burden due to RSV has not been systematically summarized in China.\nMETHOD: A systematic search was performed in the Chinese BioMedical Database (CBM), China National Knowledge Infrastructure (CNKI), Wanfang database and PubMed to identify available published RSV studies in China.\nRESULTS: A total of 489 641 patients with ARTIs from 135 studies were included in the analysis. Among patients with ARTIs, RSV accounted for 18.7% (95% confidence interval CI 17.1-20.5%). The prevalence of RSV was highest in infants (26.5%, 95% CI 23.7-29.5%) and lowest in those aged \u226516 years (2.8%, 95% CI 1.3-6.1). A higher prevalence of RSV was seen in inpatients (22%, 95% CI 19.9-24.2%) than in outpatients (14%, 95% CI 9.6-19.9%). RSV type A accounted for 63.1% (95% CI 52.3-72.8%) of all RSV infections. RSV infections occurred mainly in winter and spring. The most common clinical manifestations were cough, production of sputum, wheezing and fever.\nCONCLUSION: RSV is the leading cause of viral ARTIs in China, particularly in infants and young children. Our findings are valuable for guiding the selection of appropriate therapies for ARTIs and implementation of preventive measures against RSV infections. Our data further supports the development of a successful RSV vaccine as a high priority.',
            'year': '2015', 'book_copyright': None, 'book_publication_status': None, 'first_page': u'020417',
            'authors_str': u'Zhang Y; Yuan L; Zhang Y; Zhang X; Zheng M; Kyaw MH', 'pmc': '4676581',
            'book_contribution_date': None, 'book_editors': None, 'book_title': None,
            'title': 'Burden of respiratory syncytial virus infections in China: Systematic review and meta-analysis.',
            'grants': [], 'book_abstracts': None, 'last_page': None, 'author1_lastfm': u'ZhangY', 'pmid': '26682049',
            'issue': '2', 'book_sections': None, 'book_publisher': None, 'journal': 'J Glob Health',
            'volume_issue': u'5(2)', 'volume': '5', 'chemicals': {}, 'pubmed_type': u'article',
            'authors': [u'Zhang Y', u'Yuan L', u'Zhang Y', u'Zhang X', u'Zheng M', u'Kyaw MH'],
            'book_accession_id': None, 'pages': '020417', 'book_date_revised': None, 'doi': '10.7189/jogh.05.020417',
            'book_synonyms': None, 'url': u'http://ncbi.nlm.nih.gov/pubmed/26682049', 'author1_last_fm': u'Zhang Y',
            'issn': '2047-2986', 'book_medium': None, 'mesh': {}, 'book_history': None,
            'history': {'medline': datetime.datetime(2015, 12, 19, 0, 0),
                        'pubmed': datetime.datetime(2015, 12, 19, 0, 0),
                        'entrez': datetime.datetime(2015, 12, 19, 0, 0)}}
