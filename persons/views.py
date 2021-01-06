from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from utils.views import DefaultView
from .services import PersonService


class ProjectView(DefaultView):
    """View to render information about project authors"""

    template_name = 'project.html'
    context_object_name = 'persons'
    service = PersonService()

    def get(self, request: HttpRequest) -> HttpResponse:
        """Render page with all persons"""
        all_persons = self.service.get_all()
        return render(request, self.template_name, {
            self.context_object_name: all_persons,
        })
