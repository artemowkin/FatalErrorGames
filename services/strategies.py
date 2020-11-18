from __future__ import annotations
from typing import Any
from uuid import UUID

from djservices.strategies import BaseCRUDStrategy
from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Model, QuerySet
from django.http import Http404
from django.conf import settings


DEFAULT_LANG = settings.LANGUAGE_CODE


class BaseGETWithLangStrategy(BaseCRUDStrategy):

    """Base CRUD strategy with only GET functionality using language code

    Methods
    -------
    get_all(lang)
        Returns all model entries where `language__code` is `lang`

    get_concrete(pk, lang, default_lang)
        Returns a concrete model entry

    """

    def get_all(self, lang: str,
                default_lang: str = DEFAULT_LANG) -> QuerySet:
        entries = self.model.objects.filter(language__code=lang)
        if not entries:
            entries = self.model.objects.filter(language__code=default_lang)

        return entries

    def get_concrete(self, pk, lang: str, default_lang: str = 'en') -> Model:
        raise NotImplementedError

    def create(self, *args, **kwargs):
        raise ValueError(f"{self.__class__.__name__} can't create entries")

    def change(self, *args, **kwargs):
        raise ValueError(f"{self.__class__.__name__} can't change entries")

    def delete(self, *args, **kwargs):
        raise ValueError(f"{self.__class__.__name__} can't delete entries")


class GETStrategy(BaseGETWithLangStrategy):

    """
    CRUD strategy with get functionality using pk field
    in `get_concrete`
    """

    def get_concrete(self, pk: UUID, lang: str,
                     default_lang: str = DEFAULT_LANG) -> Model:
        try:
            entry = get_object_or_404(self.model, pk=pk, language__code=lang)
        except Http404:
            entry = get_object_or_404(
                self.model, pk=pk, language__code=default_lang
            )

        return entry


class GETSlugStrategy(BaseGETWithLangStrategy):

    """
    CRUD strategy with get functionality using slug field
    in `get_concrete`
    """

    def get_concrete(self, slug: str, lang: str,
                     default_lang: str = DEFAULT_LANG) -> Model:
        try:
            entry = get_object_or_404(
                self.model, slug=slug, language__code=lang
            )
        except Http404:
            entry = get_object_or_404(
                self.model, slug=slug, language__code=default_lang
            )

        return entry
