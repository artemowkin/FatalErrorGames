from django.shortcuts import render, redirect
from django.urls import reverse

from utils.views import DefaultView
from games.services import GameService


class NewsView(DefaultView):

    """View to return news"""

    game_service = GameService()
    template_name = 'news.html'

    def get(self, request, lang):
        """Return news page"""
        games = self.game_service.get_all()
        return render(
            request, self.template_name, {'lang': lang, 'games': games}
        )


class CooperationView(DefaultView):

    """View to return cooperation information"""

    game_service = GameService()
    template_name = 'cooperation.html'

    def get(self, request, lang):
        """Return cooperation page"""
        games = self.game_service.get_all()
        return render(
            request, self.template_name, {'lang': lang, 'games': games}
        )


class RedirectView(DefaultView):

    """View to redirect user to homepage"""

    def get(self, request):
        return redirect(reverse('news', args=(request.LANGUAGE_CODE,)))

