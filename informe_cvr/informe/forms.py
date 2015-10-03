import re

from haystack.forms import SearchForm


class EntrySearchForm(SearchForm):
    def search(self):
        sqs = super(EntrySearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()

        query = self.cleaned_data.get('q')
        if not query:
            return self.no_query_found()

        cleaned_query = re.sub('/$', '', query)

        sqs = sqs.filter(body=cleaned_query)
        return sqs
