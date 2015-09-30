from django.views import generic

from .models import Entry


class EntryDetail(generic.DetailView):
    model = Entry
    template_name = "informe/post.html"
