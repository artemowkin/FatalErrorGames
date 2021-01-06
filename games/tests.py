from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from .services import GameService
from .models import Game, GameImage


class GameModelTests(TestCase):

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

    def test_fields(self):
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

    def test_video_widget_url(self):
        self.assertEqual(
            self.game.video_widget_url, 'https://www.youtube.com/embed/test'
        )
        self.assertEqual(
            self.game.video_widget_url, 'https://www.youtube.com/embed/test'
        )


class GameServiceTests(TestCase):

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
        self.service = GameService()

    def test_get_all(self):
        all_games = self.service.get_all()
        self.assertEqual(len(all_games), 1)
        self.assertEqual(all_games[0], self.game)

    def test_get_concrete(self):
        game = self.service.get_concrete(self.game.slug)
        self.assertEqual(game, self.game)


class GameViewsTests(TestCase):

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

    def test_game_view_en(self):
        settings.LANGUAGE_CODE = 'en'
        response = self.client.get(reverse('game', args=[self.game.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game.html')
        self.assertContains(response, self.game.title)
        self.assertContains(response, self.game.preview.url)
        self.assertContains(response, self.game.short_description)
        self.assertContains(response, self.game.description)
        for game_image in self.game.images.all():
            self.assertContains(response, game_image.image.url)

    def test_game_view_ru(self):
        settings.LANGUAGE_CODE = 'ru'
        response = self.client.get(reverse('game', args=[self.game.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game.html')
        self.assertContains(response, self.game.title)
        self.assertContains(response, self.game.preview.url)
        self.assertContains(response, self.game.short_description_ru)
        self.assertContains(response, self.game.description_ru)
        for game_image in self.game.images.all():
            self.assertContains(response, game_image.image.url)
