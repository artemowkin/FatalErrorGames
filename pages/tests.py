from django.test import TestCase
from django.urls import reverse

from games.models import Game


class PagesViewsTests(TestCase):
    """Case of testing pages app views"""

    def setUp(self):
        self.game = Game.objects.create(
            title='test game',
            slug='test-game',
            preview='/static/images/cruel_galaxy_discordia_header.jpg',
            short_description='test short description',
            short_description_ru='тестовое краткое описание',
            description='test description',
            description_ru='тестовое описание',
            video="https://www.youtube.com/watch?v=test",
        )

    def test_news_view(self):
        """Test: news view returns correct response"""
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code, 200)

    def test_cooperation_view(self):
        """Test: cooperation view returns correct response"""
        response = self.client.get(reverse('cooperation'))
        self.assertEqual(response.status_code, 200)
