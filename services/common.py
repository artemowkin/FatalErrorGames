from __future__ import annotations

from django.db.models import Model, QuerySet
from django.http import Http404
from django.conf import settings


DEFAULT_LANGUAGE = settings.LANGUAGE_CODE


def get_all_model_entries_by_language(
        model: Model, language_code: str = DEFAULT_LANGUAGE) -> QuerySet:
    """Return all model entries with language code"""
    entries = model.objects.filter(language__code=language_code)
    if not entries and language_code != DEFAULT_LANGUAGE:
        entries = model.objects.filter(language__code=DEFAULT_LANGUAGE)

    return entries
