from django.db.models import QuerySet

from .models import Person


class PersonsGetService:
    """Service to get person model entries"""

    model = Person

    def get_all(self) -> QuerySet:
        """Return all persons"""
        all_persons = self.model.objects.all()
        return all_persons
