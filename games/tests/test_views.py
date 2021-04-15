
from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from ..models import Game, GameImage


class GameViewsTests(TestCase):
    """Case of testing a concrete game view"""

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
        game_image = GameImage.objects.create(
            image='/static/images/cruel_galaxy_discordia_header.jpg',
            game=self.game
        )

    def test_concrete_game_view_en(self):
        """Test: does concrete game view returns page with English game"""
        settings.LANGUAGE_CODE = 'en'
        response = self.client.get(reverse('game', args=[self.game.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game.html')

    def test_concrete_game_view_ru(self):
        """Test: does concrete game view returns page with Russian game"""
        settings.LANGUAGE_CODE = 'ru'
        response = self.client.get(reverse('game', args=[self.game.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game.html')
