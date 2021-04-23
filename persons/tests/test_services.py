from django.test import TestCase

from ..models import Person
from ..services import PersonsGetService


class PersonsGetServiceTests(TestCase):
    """Case of testing service to get persons"""

    def setUp(self):
        self.person = Person.objects.create(
            avatar='/static/images/cruel_galaxy_discordia_header.jpg',
            name='user',
            name_ru='юзер',
            profession='coder',
            profession_ru='кодер',
            about='description',
            about_ru='описание'
        )
        self.service = PersonsGetService()

    def test_get_all_model_entries(self):
        all_persons = self.service.get_all()
        self.assertEqual(len(all_persons), 1)
        self.assertEqual(all_persons[0], self.person)
