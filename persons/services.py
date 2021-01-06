from djservices import CommonCRUDService

from .models import Person


class PersonService(CommonCRUDService):
    """CRUD service with person business logic"""

    model = Person
