import re

from django.http import Http404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic
from django.views.generic.base import TemplateView

from .models import Entry
from .forms import EntrySearchForm


class Index(TemplateView):
    template_name = 'informe/index.html'


def search(request):
    form = EntrySearchForm(request.GET)
    sqs = form.search()
    if sqs:
        matched_entry = sqs[0].object
        query = re.sub('/$', '', request.GET['q'])
        return redirect('entry_detail', slug=matched_entry.slug, anchor=query)


def entry(request, slug, anchor=None):
    try:
        result = Entry.objects.get(slug=slug)
    except Entry.DoesNotExist:
        raise Http404('esa entrada no existe')

    if anchor:
        print(anchor)
        result.body_html = re.sub(anchor, '<span class="highlight">{0}</span>'.format(anchor),
                                  result.body_html, flags=re.I)
    template_name = "informe/post.html"
    return render(request, template_name, {'result': result})
