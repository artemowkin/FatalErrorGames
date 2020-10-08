from django.shortcuts import render

from utils.views import DefaultView
from games.services import GameService
from .services import PersonService


class ProjectView(DefaultView):

    """View to return information about project"""

    game_service = GameService()
    person_service = PersonService()
    template_name = 'project.html'

    def get(self, request, lang):
        """Return page with persons"""
        games = self.game_service.get_all()
        persons = self.person_service.get_all()
        return render(
            request, self.template_name, {
                'games': games, 'persons': persons, 'lang': lang
            }
        )

