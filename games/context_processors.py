from .services import GameService
from .models import Game


def games_processor(request):
    """Add all games in each context"""
    game_service = GameService()
    all_games = game_service.get_all()
    return {'games': all_games}
