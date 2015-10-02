from django.views import generic
from django.views.generic.base import TemplateView

from .models import Entry


class Index(TemplateView):
    template_name = 'informe/index.html'


class EntryDetail(generic.DetailView):
    model = Entry
    template_name = "informe/post.html"
