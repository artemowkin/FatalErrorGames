from django.shortcuts import get_object_or_404
from django.db.models import QuerySet

from .models import Game


class GamesGetService:
    """Service to get game model entries"""

    model = Game

    def get_all(self) -> QuerySet:
        """Return all game model entries"""
        all_games = self.model.objects.all()
        return all_games

    def get_concrete(self, slug: str) -> Game:
        """Return a concrete game using slug"""
        game = get_object_or_404(Game, slug=slug)
        return game
