import services.common as services_common
from .models import Game


def games_processor(request):
    """Add all games in each context"""
    all_games = services_common.get_all_model_entries(Game)
    return {'games': all_games}
