from django.db.models import Model
from django.shortcuts import get_object_or_404
from djservices.strategies import CommonCRUDStrategy


class GetBySlugCRUDStrategy(CommonCRUDStrategy):
    """Common CRUD strategy with edited get_concrete method to get entry
    using slug field
    """

    def get_concrete(self, slug: str) -> Model:
        """Return a concrete model entry using slug field"""
        return get_object_or_404(self.model, slug=slug)
