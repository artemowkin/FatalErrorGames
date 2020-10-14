from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse

from utils.views import DefaultView
from games.services import GameService


class PageView(DefaultView):

    """Base view for all simple page views

    Attributes
    ----------
    game_service : GameService
        Game service to work with Game model entries
    template_name : str
        Name of template to render

    Methods
    -------
    get(request, lang)
        Render template

    """

    game_service = GameService()
    template_name = None

    def get(self, request: HttpRequest, lang: str) -> HttpResponse:
        """Render template with games and language code"""
        games = self.game_service.get_all()
        return render(
            request, self.template_name, {'lang': lang, 'games': games}
        )


class NewsView(PageView):

    """View to return news"""

    template_name = 'news.html'


class CooperationView(PageView):

    """View to return cooperation information"""

    template_name = 'cooperation.html'


class RedirectView(DefaultView):

    """View to redirect user to homepage

    Methods
    -------
    get(request)
        Redirect user

    """

    def get(self, request: HttpRequest) -> HttpResponse:
        """Redirect user to news page with user's language"""
        return redirect(reverse('news', args=(request.LANGUAGE_CODE,)))
