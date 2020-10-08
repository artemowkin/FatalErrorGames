from __future__ import annotations
from abc import ABC
from uuid import UUID

from django.db.models import QuerySet, Model
from django.shortcuts import get_object_or_404


class BaseStrategy(ABC):

    """Base strategy class"""

    def __init__(self, model) -> None:
        self._model = model


class SimpleGetStrategy(BaseStrategy):

    def get_all(self) -> QuerySet:
        """Return all model entries"""
        return self._model.objects.all()

    def get_concrete(self, pk: UUID) -> Model:
        """Return a concrete entry with pk"""
        entry = get_object_or_404(self._model, pk=pk)
        return entry

