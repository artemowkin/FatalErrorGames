from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from . import services
from utils.views import DefaultView


class GameView(DefaultView):
    """View to render a concrete game page"""

    template_name = 'game.html'
    context_object_name = 'game'

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        game = services.get_concrete_game_by_slug(
            slug, request.LANGUAGE_CODE
        )
        return render(request, self.template_name, {
            self.context_object_name: game,
        })
