from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from utils.views import DefaultView
from games.services import GameService
from .services import PersonService


class ProjectView(DefaultView):

    """View to return information about project authors

    Attributes
    ----------
    game_service : GameService
        Game service to work with Game model entries
    person_service : PersonService
        Person service to work with Person model entries
    template_name : str
        Name of template to render

    """

    game_service = GameService()
    person_service = PersonService()
    template_name = 'project.html'

    def get(self, request: HttpRequest, lang: str) -> HttpResponse:
        """Render page with persons, games list and language code"""
        games = self.game_service.get_all()
        persons = self.person_service.get_all()
        return render(
            request, self.template_name, {
                'games': games, 'persons': persons, 'lang': lang
            }
        )

