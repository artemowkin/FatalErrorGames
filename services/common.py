from __future__ import annotations

from django.db.models import Model, QuerySet

from utils.logs import handle_services_exceptions


@handle_services_exceptions
def get_all_model_entries(model: Model) -> QuerySet:
    """Return all model entries"""
    return model.objects.all()
