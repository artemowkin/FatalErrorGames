from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

import services.common as services_common
from utils.views import DefaultView
from .models import Person


class ProjectView(DefaultView):
    """View to render information about project authors"""

    model = Person
    template_name = 'project.html'
    context_object_name = 'persons'

    def get(self, request: HttpRequest) -> HttpResponse:
        """Render page with all persons"""
        all_persons = services_common.get_all_model_entries(self.model)
        return render(request, self.template_name, {
            self.context_object_name: all_persons,
        })
