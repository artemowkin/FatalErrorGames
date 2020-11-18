from djservices.base import BaseCRUDService

from services import GETSlugStrategy
from .models import Game


class GameService(BaseCRUDService):

    """Game service

    Attributes
    ----------
    strategy_class : SimpleGetStrategy
        Strategy class with get functionality
    model : Game
        Game model service work with

    """

    strategy_class = GETSlugStrategy
    model = Game
