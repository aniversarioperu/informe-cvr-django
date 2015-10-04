import os

from django.test import TestCase
from django.test.client import Client
from django.conf import settings

from informe.models import Entry


TEST_FILE = os.path.join(settings.BASE_DIR, '..', '..', 'source_files',
                         'prefacio.md')


class TestViews(TestCase):
    def setUp(self):
        self.c = Client()
        with open(TEST_FILE, 'r') as handle:
            prefacio = handle.read()
            e = Entry(title='PREFACIO', body=prefacio, slug='prefacio')
            e.save()

    def test_index(self):
        result = self.c.get('/')
        self.assertEqual(200, result.status_code)

    def test_search(self):
        result = self.c.get('/search/?q=historia', follow=True)
        self.assertEqual(200, result.status_code)
