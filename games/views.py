from uuid import UUID

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from utils.views import DefaultView
from .services import GameService
from langs.models import Language


class GameView(DefaultView):

    """View to return information about game"""

    game_service = GameService()
    template_name = 'game.html'

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        """
        Render a concrete game page
        """
        game = self.game_service.get_concrete(slug, request.LANGUAGE_CODE)
        return render(request, self.template_name, {'game': game})
