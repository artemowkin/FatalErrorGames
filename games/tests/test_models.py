from django.test import TestCase

from ..models import Game


class GameModelTests(TestCase):
    """Case of testing game model"""

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

    def test_created_game_fields_valid(self):
        """Test: are created game fields valid"""
        self.assertEqual(self.game.title, 'test game')
        self.assertEqual(self.game.slug, 'test-game')
        self.assertEqual(
            self.game.preview.url,
            '/media/static/images/cruel_galaxy_discordia_header.jpg'
        )
        self.assertEqual(
            self.game.short_description, 'test short description'
        )
        self.assertEqual(
            self.game.short_description_ru, 'тестовое краткое описание'
        )
        self.assertEqual(self.game.description, 'test description')
        self.assertEqual(self.game.description_ru, 'тестовое описание')
        self.assertEqual(
            self.game.video, 'https://www.youtube.com/watch?v=test'
        )

    def test_video_widget_url_parameter(self):
        """Test: does video_widget_url parameter work correct"""
        self.assertEqual(
            self.game.video_widget_url, 'https://www.youtube.com/embed/test'
        )
        self.assertEqual(
            self.game.video_widget_url, 'https://www.youtube.com/embed/test'
        )
