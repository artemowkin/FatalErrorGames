from services import BaseGetService
from services.strategies import SimpleGetStrategy

from .models import Person


class PersonService(BaseGetService):

    """Person service

    Attributes
    ----------
    strategy_class : SimpleGetStrategy
        Strategy class with get functionality
    model : Person
        Person model service work with

    """

    strategy_class = SimpleGetStrategy
    model = Person
