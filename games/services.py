from __future__ import annotations

from django.shortcuts import get_object_or_404
from django.db.models import Model
from django.http import Http404
from django.conf import settings

from .models import Game


DEFAULT_LANGUAGE = settings.LANGUAGE_CODE


def get_concrete_game_by_slug(
        game_slug: str, language_code: str = DEFAULT_LANGUAGE) -> Model:
    """Return a concrete game entry with slug and language_code"""
    try:
        return get_object_or_404(
            Game, slug=game_slug, language__code=language_code
        )
    except Http404:
        if language_code != DEFAULT_LANGUAGE:
            return get_object_or_404(
                Game, slug=game_slug, language__code=DEFAULT_LANGUAGE
            )

        raise
