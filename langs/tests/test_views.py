import simplejson as json

from django.test import TestCase
from django.urls import reverse


class LanguageViewsTests(TestCase):
    """Case of testing language views"""

    def test_setlang(self):
        """Test: does setlang view return correct response"""
        response = self.client.post(
            reverse('set_language'), {'language': 'en'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response_status = json.loads(response.content).get('status')
        self.assertEqual(response_status, 'ok')
