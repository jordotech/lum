from lum.forms import PubMedForm
from django.shortcuts import render_to_response, render
from metapub import PubMedFetcher
from datetime import datetime
def home(request):

    ctx = {}

    if request.method == "POST":
        form = PubMedForm(request.POST)
        if form.is_valid():
            keywords = form.cleaned_data['keywords']
            f = PubMedFetcher()
            pmids = f.pmids_for_query(keywords)
            pmid_list = []
            for pmid in pmids[:40]:
                data = f.article_by_pmid(pmid).to_dict()
                print data['title']
                row = {
                    'pmid': data['pmid'],
                    'title': data['title'],
                }
                try:
                    row['date'] = data['history']['pubmed']
                except:
                    row['date'] = datetime.now()
                pmid_list.append(row)
            ctx['keywords'] = keywords
            ctx['pmids'] = pmids
            ctx['pmid_list'] = pmid_list
            ctx['result_count'] = len(pmids)
    else:
        form = PubMedForm()
    ctx['form'] = form
    return render(request, 'lum/home.html', ctx)