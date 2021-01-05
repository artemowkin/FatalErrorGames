from __future__ import annotations

from django.shortcuts import get_object_or_404
from django.db.models import Model

from .models import Game
from utils.logs import handle_services_exceptions


@handle_services_exceptions
def get_concrete_game_by_slug(game_slug: str) -> Model:
    """Return a concrete game entry with slug"""
    return get_object_or_404(Game, slug=game_slug)
