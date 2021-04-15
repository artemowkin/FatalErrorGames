from django.test import TestCase

from ..models import Game
from ..services import GameService


class GameServiceTests(TestCase):
    """Case of testing game service"""

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

    def test_get_all_returns_all_games(self):
        """Test: does service get_all method return all games"""
        all_games = self.service.get_all()
        self.assertEqual(len(all_games), 1)
        self.assertEqual(all_games[0], self.game)

    def test_get_concrete_returns_a_concrete_game(self):
        """Test: does service get_concrete method return a
        concrete game by slug
        """
        game = self.service.get_concrete(self.game.slug)
        self.assertEqual(game, self.game)
