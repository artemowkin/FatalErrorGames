import json

from django.test import TestCase
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse

from . import services
from .models import Language


User = get_user_model()


class LanguageServicesTests(TestCase):

    def setUp(self):
        self.language = Language.objects.create(code='en')
        User.objects.create_superuser(
            username='testuser', password='testpass'
        )
        self.client.login(username='testuser', password='testpass')

    def test_is_language_code_correct(self):
        correct = services.is_language_code_correct('en')
        self.assertTrue(correct)
        incorrect = services.is_language_code_correct('ru')
        self.assertFalse(incorrect)

    def test_set_language_session(self):
        session = self.client.session
        services.set_language_session(session, 'en')
        self.assertEqual(session[LANGUAGE_SESSION_KEY], 'en')

    def test_set_response_language_cookie(self):
        response = HttpResponse("message")
        services.set_response_language_cookie(response, 'en')
        language_cookie = response.cookies[settings.LANGUAGE_COOKIE_NAME]
        self.assertEqual(
            language_cookie.value, 'en'
        )


class LanguageViewsTests(TestCase):

    def setUp(self):
        self.language = Language.objects.create(code='en')

    def test_setlang(self):
        response = self.client.post(
            reverse('set_language'), {'language': 'en'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        response_status = json.loads(response.content).get('status')
        self.assertEqual(response_status, 'ok')
