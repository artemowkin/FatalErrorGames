from django.test import TestCase
from django.urls import reverse

from games.models import Game


class PagesViewsTests(TestCase):

    def setUp(self):
        self.game = Game.objects.create(
            title='test_game',
            preview='/static/images/cruel_galaxy_discordia_header.jpg',
            short_description='test_english_description',
            short_description_ru='тестовое_русское_описание',
            description='test_english_description',
            description_ru='тестовое_русское_описание',
            video="https://www.youtube.com/watch?v=test"
        )

    def test_news_view(self):
        response = self.client.get(reverse('news', args=['en']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.game.title)

    def test_cooperation_view(self):
        response = self.client.get(reverse('cooperation', args=['en']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.game.title)
