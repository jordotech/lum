
from lum.forms import PubMedForm
from django.shortcuts import render_to_response, render
from metapub import PubMedFetcher
from datetime import datetime
#from metapub.utils import asciify

from lum.models import Publication
def home(request):
    ctx = {}

    return render(request, 'lum/home.html', ctx)


def search(request):
    ctx = {}
    f = PubMedFetcher()
    if request.method == "POST":
        form = PubMedForm(request.POST)
        if form.is_valid():
            keywords = form.cleaned_data['keywords']

            pmids = f.pmids_for_query(keywords)
            for pmid in pmids:
                new_pmid = Publication.objects.get_or_create(pmid=pmid)
                if new_pmid[1]:
                    pass  # newly created
            pmid_list = []
            '''
            for pmid in pmids[:10]:

                data = f.article_by_pmid(pmid).to_dict()

                row = {
                    'pmid': data['pmid'],
                    'title': data['title'],
                }
                try:
                    row['date'] = data['history']['pubmed']
                except:
                    row['date'] = datetime.now()
                pmid_list.append(row)
            '''
            for pmid in pmids:
                row = {
                    'pmid':pmid,
                }
                pmid_list.append(row)
            ctx['keywords'] = keywords
            ctx['pmids'] = pmids
            ctx['pmid_list'] = pmid_list
            ctx['result_count'] = len(pmids)
    else:
        initial = {}
        if request.GET.get('keywords', None):
            initial['keywords'] = request.GET.get('keywords')
        form = PubMedForm(initial=initial)
    ctx['form'] = form
    return render(request, 'lum/search.html', ctx)


