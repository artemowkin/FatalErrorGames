from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from .models import Game, GameImage
from .services import GameService
from langs.models import Language


class GameModelTests(TestCase):

    def setUp(self):
        self.language = Language.objects.create(code='en')
        self.game = Game.objects.create(
            title='test game',
            slug='test-game',
            preview='/static/images/cruel_galaxy_discordia_header.jpg',
            short_description='test short description',
            description='test description',
            video="https://www.youtube.com/watch?v=test",
            language=self.language
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
        self.assertEqual(self.game.description, 'test description')
        self.assertEqual(
            self.game.video, 'https://www.youtube.com/watch?v=test'
        )
        self.assertEqual(self.game.language, self.language)

    def test_video_widget_url(self):
        self.assertEqual(
            self.game.video_widget_url, 'https://www.youtube.com/embed/test'
        )
        self.assertEqual(
            self.game.video_widget_url, 'https://www.youtube.com/embed/test'
        )


class GameServiceTests(TestCase):

    def setUp(self):
        self.lang = Language.objects.create(code='en')
        self.game = Game.objects.create(
            title='test game',
            slug='test-game',
            preview='/static/images/cruel_galaxy_discordia_header.jpg',
            short_description='test short description',
            description='test description',
            video="https://www.youtube.com/watch?v=test",
            language=self.lang,
        )
        self.service = GameService()

    def test_get_all(self):
        all_games = self.service.get_all()
        self.assertEqual(len(all_games), 1)
        self.assertEqual(all_games[0], self.game)

    def test_get_all_ru(self):
        all_games = self.service.get_all('ru')
        self.assertEqual(len(all_games), 1)
        self.assertEqual(all_games[0], self.game)

    def test_get_all_ru_with_ru_game(self):
        lang_ru = Language.objects.create(code='ru')
        game_ru = Game.objects.create(
            title='test game',
            slug='test-game',
            preview='/static/images/cruel_galaxy_discordia_header.jpg',
            short_description='Тестовое короткое описание',
            description='Тестовое описание',
            video="https://www.youtube.com/watch?v=test",
            language=lang_ru
        )
        all_games = self.service.get_all('ru')
        self.assertEqual(len(all_games), 1)
        self.assertEqual(all_games[0], game_ru)

    def test_get_concrete(self):
        entry = self.service.get_concrete(
            self.game.slug, self.game.language.code
        )
        self.assertEqual(entry, self.game)

    def test_get_concrete_ru(self):
        entry = self.service.get_concrete(self.game.slug, 'ru')
        self.assertEqual(entry, self.game)

    def test_get_concrete_ru_with_game_ru(self):
        lang_ru = Language.objects.create(code='ru')
        game_ru = Game.objects.create(
            title='test game',
            slug='test-game',
            preview='/static/images/cruel_galaxy_discordia_header.jpg',
            short_description='Тестовое короткое описание',
            description='Тестовое описание',
            video="https://www.youtube.com/watch?v=test",
            language=lang_ru
        )
        entry = self.service.get_concrete(game_ru.slug, lang_ru.code)
        self.assertEqual(entry, game_ru)


class GameViewsTest(TestCase):

    def setUp(self):
        self.lang = Language.objects.create(code='en')
        self.lang_ru = Language.objects.create(code='ru')
        self.game = Game.objects.create(
            title='test game',
            slug='test-game',
            preview='/static/images/cruel_galaxy_discordia_header.jpg',
            short_description='test short description',
            description='test description',
            video="https://www.youtube.com/watch?v=test",
            language=self.lang
        )
        self.game_ru = Game.objects.create(
            title='test game',
            slug='test-game',
            preview='/static/images/cruel_galaxy_discordia_header.jpg',
            short_description='Тестовое краткое описание',
            description='Тестовое описание',
            video="https://www.youtube.com/watch?v=test",
            language=self.lang_ru
        )
        game_image = GameImage.objects.create(
            image='/static/images/cruel_galaxy_discordia_header.jpg',
            game=self.game
        )
        game_image = GameImage.objects.create(
            image='/static/images/cruel_galaxy_discordia_header.jpg',
            game=self.game_ru
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
        response = self.client.get(reverse('game', args=[self.game_ru.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game.html')
        self.assertContains(response, self.game_ru.title)
        self.assertContains(response, self.game_ru.preview.url)
        self.assertContains(response, self.game_ru.short_description)
        self.assertContains(response, self.game_ru.description)
        for game_image in self.game_ru.images.all():
            self.assertContains(response, game_image.image.url)
