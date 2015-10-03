import re

from django.http import Http404
from django.shortcuts import redirect
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
        return redirect('entry_detail', slug=matched_entry.slug)


class EntryDetail(generic.DetailView):
    model = Entry
    template_name = "informe/post.html"
