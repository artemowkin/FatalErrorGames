from __future__ import annotations
from abc import ABC

from django.core.exceptions import ImproperlyConfigured
from django.db.models import QuerySet, Model


class BaseGetService(ABC):

    """Base service to get entries

    Attributes
    ----------
    strategy_class
        Strategy class with get functionality
    model
        Model service work with

    Methods
    -------
    get_all(*args, **kwargs)
        Return all entries
    get_concrete(*args, **kwargs)
        Return a concrete entry

    """

    strategy_class = None
    model = None

    def __init__(self) -> None:
        if not all((self.strategy_class, self.model)):
            raise ImproperlyConfigured("You need to set `strategy` attribute")

        self._strategy = self.strategy_class(self.model)

    def get_concrete(self, *args, **kwargs) -> Model:
        """Return a concrete entry"""
        return self._strategy.get_concrete(*args, **kwargs)

    def get_all(self, *args, **kwargs) -> QuerySet:
        """Return all entries"""
        return self._strategy.get_all(*args, **kwargs)

