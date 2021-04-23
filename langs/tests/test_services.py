from django.test import TestCase
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.conf import settings

from .. import services


User = get_user_model()


class LanguageServicesTests(TestCase):
    """Case of testing language services"""

    def setUp(self):
        User.objects.create_superuser(
            username='testuser', password='testpass'
        )
        self.client.login(username='testuser', password='testpass')

    def test_set_language_session(self):
        """Test: does set_language_session function work correctly"""
        session = self.client.session
        services.set_language_session(session, 'en')
        self.assertEqual(session[LANGUAGE_SESSION_KEY], 'en')

    def test_set_response_language_cookie(self):
        """Test: does set_response_language_cookie work correctly"""
        response = HttpResponse("message")
        services.set_response_language_cookie(response, 'en')
        language_cookie = response.cookies[settings.LANGUAGE_COOKIE_NAME]
        self.assertEqual(
            language_cookie.value, 'en'
        )
