from uuid import UUID

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from utils.views import DefaultView
from .services import GameService


class GameView(DefaultView):

    """View to return information about game"""

    game_service = GameService()
    template_name = 'game.html'

    def get(self, request: HttpRequest, lang: str, pk: UUID) -> HttpResponse:
        """
        Render game page with games list, concrete game and language code
        """
        game = self.game_service.get_concrete(pk)
        games = self.game_service.get_all()
        return render(
            request, self.template_name,
            {'games': games, 'game': game, 'lang': lang}
        )
