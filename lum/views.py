
from lum.forms import PubMedForm
from django.shortcuts import render_to_response, render
from metapub import PubMedFetcher
from django.http import HttpResponseRedirect
from datetime import datetime
#from metapub.utils import asciify
import logging
logger = logging.getLogger('lum')
from lum.models import Publication, SearchStash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    ctx = {}
    return render(request, 'lum/home.html', ctx)

@login_required
def saved_searches(request, pk=None):

    ctx = {
        'list' : []
    }
    if not pk:
        saved_searches = SearchStash.objects.filter(user=request.user)
        for s in saved_searches:
            ctx['list'].append(s)
        return render(request, 'lum/saved_searches.html', ctx)
    else:
        saved_search = SearchStash.objects.get(pk=pk)
        ctx['obj'] = saved_search
    return render(request, 'lum/saved_search.html', ctx)

@login_required
def save_user_query(request, query=None):
    query = query.replace('/','')
    SearchStash.objects.create(search_used=query, user=request.user)
    url = '/search/?q=%s' % query
    return HttpResponseRedirect(url)

@login_required
def save_pmid_to_query(request, query_id, pmid):
    pub = Publication.objects.get_or_create(pmid=pmid)[0]
    query = SearchStash.objects.get(pk=query_id)
    query.pmids.add(pub)
    url = '/search/?q=%s' % query.search_used
    return HttpResponseRedirect(url)

@login_required
def delete_user_query(request, pk):

    SearchStash.objects.filter(pk=pk, user=request.user).delete()
    next = request.GET.get('next', None)
    if next:
        return HttpResponseRedirect(next)
    else:
        return HttpResponseRedirect('/saved-searches/')

@login_required
def search(request):
    ctx = {
        'query_saved' : None,
        'saved_pmids':[],
        'total_saved_queries':SearchStash.objects.filter(user=request.user).count(),
    }
    f = PubMedFetcher()
    initial = {}
    query_saved = None
    try:
        query_saved = SearchStash.objects.get(search_used=request.GET.get('q'))
    except: pass
    else:
        ctx['saved_pmids'] = [pub.pmid for pub in query_saved.pmids.all()]
        ctx['query_saved'] = query_saved

    if not ctx['query_saved'] and request.GET.get('q'):
        messages.add_message(request, messages.INFO, '<strong>Note:</strong> You must click "Save Query" above to start capturing publications for this query.')
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


