from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .services import GameService
from utils.views import DefaultView


class GameView(DefaultView):
    """View to render a concrete game page"""

    template_name = 'game.html'
    context_object_name = 'game'
    service = GameService()

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        game = self.service.get_concrete(slug)
        return render(request, self.template_name, {
            self.context_object_name: game,
        })
