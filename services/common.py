from __future__ import annotations

from django.db.models import Model, QuerySet


def get_all_model_entries(model: Model) -> QuerySet:
    """Return all model entries"""
    return model.objects.all()
