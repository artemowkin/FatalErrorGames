from djservices.base import BaseCRUDService

from .models import Game
from services.strategies import GetBySlugCRUDStrategy


class GameService(BaseCRUDService):
    """CRUD service with Game business logic"""

    strategy_class = GetBySlugCRUDStrategy
    model = Game
