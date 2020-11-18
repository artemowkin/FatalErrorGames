from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from utils.views import DefaultView
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

    person_service = PersonService()
    template_name = 'project.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        """Render page with persons and games list"""
        persons = self.person_service.get_all(request.LANGUAGE_CODE)
        return render(request, self.template_name, {'persons': persons})
