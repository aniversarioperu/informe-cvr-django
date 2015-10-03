import datetime

from haystack import indexes

from informe.models import Entry


class EntryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    body = indexes.CharField(model_attr='body')

    def get_model(self):
        return Entry
