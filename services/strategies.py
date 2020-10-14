from __future__ import annotations
from abc import ABC
from uuid import UUID
import logging

from django.db.models import QuerySet, Model
from django.shortcuts import get_object_or_404
from django.http import Http404


logger = logging.getLogger(__name__)


class BaseStrategy(ABC):

    """Base strategy class"""

    def __init__(self, model) -> None:
        logger.info(
            f"{self.__class__.__name__}.__init__() "
            f"got a model: {model.__name__}"
        )
        self._model = model


class SimpleGetStrategy(BaseStrategy):

    def get_all(self) -> QuerySet:
        """Return all model entries"""
        logger.info(
            f"Calling {self.__class__.__name__}.get_all()"
        )

        try:
            return self._model.objects.all()
        except Exception:
            logger.exception(
                f"Problem with getting all {self._model.__name__} entries "
                f"in method {self.__class__.__name__}.get_all()"
            )
            raise

    def get_concrete(self, pk: UUID) -> Model:
        """Return a concrete entry with pk"""
        logger.info(
            f"Calling {self.__class__.__name__}.get_concrete() with "
            f"pk == {pk}"
        )

        try:
            entry = get_object_or_404(self._model, pk=pk)
        except Http404:
            logger.warning(
                f"404 Not Found for model {self._model.__name__} "
                f"and pk == {pk}"
            )
            raise
        except Exception:
            logger.exception(
                f"Problem with getting a concrete entry of model "
                f"{self._model.__name__} with pk == {pk}"
            )
            raise

        return entry

