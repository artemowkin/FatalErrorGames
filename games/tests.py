from django.test import TestCase
from django.urls import reverse

from .models import Game, GameImage
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


class GameViewsTest(TestCase):

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
        game_image = GameImage.objects.create(
            image='/static/images/cruel_galaxy_discordia_header.jpg',
            game=self.game
        )

    def test_game_view_en(self):
        response = self.client.get(reverse('game', args=['en', self.game.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game.html')
        self.assertContains(response, self.game.title)
        self.assertContains(response, self.game.preview.url)
        self.assertContains(response, self.game.short_description)
        self.assertContains(response, self.game.description)
        for game_image in self.game.images.all():
            self.assertContains(response, game_image.image.url)

    def test_game_view_ru(self):
        response = self.client.get(reverse('game', args=['ru', self.game.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game.html')
        self.assertContains(response, self.game.title)
        self.assertContains(response, self.game.preview.url)
        self.assertContains(response, self.game.short_description_ru)
        self.assertContains(response, self.game.description_ru)
        for game_image in self.game.images.all():
            self.assertContains(response, game_image.image.url)
