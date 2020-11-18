from djservices.base import BaseCRUDService

from services import GETStrategy
from .models import Person


class PersonService(BaseCRUDService):

    """Person service

    Attributes
    ----------
    strategy_class : SimpleGetStrategy
        Strategy class with get functionality
    model : Person
        Person model service work with

    """

    strategy_class = GETStrategy
    model = Person
