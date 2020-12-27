from __future__ import annotations
from typing import Any
from uuid import UUID

from django.shortcuts import get_object_or_404, get_list_or_404
from django.db.models import Model, QuerySet
from django.http import Http404
from django.conf import settings


DEFAULT_LANG = settings.LANGUAGE_CODE


def get_all_by_language(
        model: Model, language_code: str = DEFAULT_LANG) -> QuerySet:
    """Return all model entries with language code"""
    entries = model.objects.filter(language__code=language_code)
    if not entries and language_code != DEFAULT_LANG:
        entries = model.objects.filter(language__code=DEFAULT_LANG)

    return entries


def get_concrete_by_pk(
        model: Model, pk: UUID, language_code: str = DEFAULT_LANG) -> Model:
    """Return a concrete model entry with pk and language code"""
    try:
        return get_object_or_404(model, pk=pk, language__code=language_code)
    except Http404:
        if language_code != DEFAULT_LANG:
            return get_object_or_404(
                model, pk=pk, language__code=DEFAULT_LANG
            )

        raise


def get_concrete_by_slug(
        model: Model, slug: str, language_code: str = DEFAULT_LANG) -> Model:
    """Return a concrete model entry with slug and language_code"""
    try:
        return get_object_or_404(
            model, slug=slug, language__code=language_code
        )
    except Http404:
        if language_code != DEFAULT_LANG:
            return get_object_or_404(
                model, slug=slug, language__code=DEFAULT_LANG
            )

        raise
