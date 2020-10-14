from services import BaseGetService
from services.strategies import SimpleGetStrategy

from .models import Game


class GameService(BaseGetService):

    """Game service

    Attributes
    ----------
    strategy_class : SimpleGetStrategy
        Strategy class with get functionality
    model : Game
        Game model service work with

    """

    strategy_class = SimpleGetStrategy
    model = Game
