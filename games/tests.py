from django.test import TestCase

from .models import Game
from .services import GameService


class GameModelTests(TestCase):

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

    def test_fields(self):
        self.assertEqual(self.game.title, 'test_game')
        self.assertEqual(
            self.game.preview.url,
            '/media/static/images/cruel_galaxy_discordia_header.jpg'
        )
        self.assertEqual(
            self.game.short_description, 'test_english_description'
        )
        self.assertEqual(
            self.game.short_description_ru, 'тестовое_русское_описание'
        )
        self.assertEqual(self.game.description, 'test_english_description')
        self.assertEqual(
            self.game.description_ru, 'тестовое_русское_описание'
        )
        self.assertEqual(
            self.game.video, 'https://www.youtube.com/watch?v=test'
        )

    def test_video_widget_url(self):
        self.assertEqual(
            self.game.video_widget_url, 'https://www.youtube.com/embed/test'
        )


class TestGameService(TestCase):

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
        self.service = GameService()

    def test_get_all(self):
        all_games = self.service.get_all()
        self.assertEqual(len(all_games), 1)
        self.assertEqual(all_games[0], self.game)

    def test_get_concrete(self):
        entry = self.service.get_concrete(self.game.pk)
        self.assertEqual(entry, self.game)
