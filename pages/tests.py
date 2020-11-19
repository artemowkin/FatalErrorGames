from django.test import TestCase
from django.urls import reverse

from games.models import Game
from langs.models import Language


class PagesViewsTests(TestCase):

    def setUp(self):
        lang = Language.objects.create(code='en')
        self.game = Game.objects.create(
            title='test game',
            slug='test-game',
            preview='/static/images/cruel_galaxy_discordia_header.jpg',
            short_description='test short description',
            description='test description',
            video="https://www.youtube.com/watch?v=test",
            language=lang
        )

    def test_news_view(self):
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.game.title)

    def test_cooperation_view(self):
        response = self.client.get(reverse('cooperation'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.game.title)
