
from lum.forms import PubMedForm
from django.shortcuts import render_to_response, render
from metapub import PubMedFetcher
from datetime import datetime
#from metapub.utils import asciify

from lum.models import Publication
from django.contrib.auth.decorators import login_required

def home(request):
    ctx = {}
    return render(request, 'lum/home.html', ctx)

@login_required
def search(request):
    ctx = {}
    f = PubMedFetcher()
    initial = {}
    if request.GET.get('q', None):
        keywords = request.GET.get('q', None)
        initial['q'] = request.GET.get('q')
        pmids = f.pmids_for_query(query=keywords, retmax=100)
        pmid_list = []
        for pmid in pmids:
            new_pmid = Publication.objects.get_or_create(pmid=pmid)[0]
            row = {
                'pmid': new_pmid.pmid,
            }
            pmid_list.append(row)
        ctx['keywords'] = keywords
        ctx['pmids'] = pmids
        ctx['pmid_list'] = pmid_list
        ctx['result_count'] = len(pmids)
    form = PubMedForm(initial=initial)
    ctx['form'] = form
    return render(request, 'lum/search.html', ctx)


