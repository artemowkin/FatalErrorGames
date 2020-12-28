import services.common as services_common
from .models import Game


def games_processor(request):
    """Add all games in each context"""
    games = services_common.get_all_model_entries_by_language(
        Game, request.LANGUAGE_CODE
    )
    return {'games': games}
