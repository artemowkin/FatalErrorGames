from .services import GamesGetService


def games_processor(request):
    """Add all games in context"""
    game_service = GamesGetService()
    all_games = game_service.get_all()
    return {'games': all_games}
