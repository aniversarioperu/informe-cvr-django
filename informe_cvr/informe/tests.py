from django.test import TestCase
from django.test.client import Client


class TestViews(TestCase):
    def setUp(self):
        self.c = Client()

    def test_index(self):
        result = self.c.get('/')
        self.assertEqual(200, result.status_code)

