from uuid import UUID

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import services.common as services_common
from utils.views import DefaultView
from langs.models import Language
from .models import Game


class GameView(DefaultView):
    """View to render a concrete game page"""

    model = Game
    template_name = 'game.html'
    context_object_name = 'game'

    def get(self, request: HttpRequest, slug: str) -> HttpResponse:
        game = services_common.get_concrete_by_slug(
            self.model, slug, request.LANGUAGE_CODE
        )
        return render(request, self.template_name, {
            self.context_object_name: game,
        })
