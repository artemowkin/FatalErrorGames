from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import services.common as services_common
from utils.views import DefaultView
from .models import Person


class ProjectView(DefaultView):
    """View to render information about project authors

    Attributes
    ----------
    game_service : GameService
        Game service to work with Game model entries
    person_service : PersonService
        Person service to work with Person model entries
    template_name : str
        Name of template to render

    """

    model = Person
    template_name = 'project.html'
    context_object_name = 'persons'

    def get(self, request: HttpRequest) -> HttpResponse:
        """Render page with persons and games list"""
        persons = services_common.get_all_model_entries_by_language(
            self.model, request.LANGUAGE_CODE
        )
        return render(request, self.template_name, {
            self.context_object_name: persons,
        })
