"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import json

class PasSiSimpleTest(TestCase):

    def test_auto_completion(self):
        """
        Test l'auto-completion
        """
        from django.test.client import Client
        c = Client()
        response = c.get('/search/', {'q': 'veo'})
        self.assertEqual(response.status_code, 200)
        content = json.loads(response.content)
        self.assertEqual(content[0]['symbol'], "VIE.PA")