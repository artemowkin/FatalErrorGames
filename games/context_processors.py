from .services import GameService


def games_processor(request):
    service = GameService()
    games = service.get_all(request.LANGUAGE_CODE)
    return {'games': games}
