from django.test import TestCase

from .models import Person
from .services import PersonService


class PersonModelTests(TestCase):

    def setUp(self):
        self.person = Person.objects.create(
            avatar='/static/images/cruel_galaxy_discordia_header.jpg',
            name='user', name_ru='юзер',
            profession='coder', profession_ru='кодер',
            about='description', about_ru='описание'
        )

    def test_fields(self):
        self.assertEqual(
            self.person.avatar.url,
            '/media/static/images/cruel_galaxy_discordia_header.jpg'
        )
        self.assertEqual(self.person.name, 'user')
        self.assertEqual(self.person.name_ru, 'юзер')
        self.assertEqual(self.person.profession, 'coder')
        self.assertEqual(self.person.profession_ru, 'кодер')
        self.assertEqual(self.person.about, 'description')
        self.assertEqual(self.person.about_ru, 'описание')


class PersonServiceTests(TestCase):

    def setUp(self):
        self.person = Person.objects.create(
            avatar='/static/images/cruel_galaxy_discordia_header.jpg',
            name='user', name_ru='юзер',
            profession='coder', profession_ru='кодер',
            about='description', about_ru='описание'
        )
        self.service = PersonService()

    def test_get_all(self):
        all_entries = self.service.get_all()
        self.assertEqual(len(all_entries), 1)
        self.assertEqual(all_entries[0], self.person)

    def test_get_concrete(self):
        entry = self.service.get_concrete(self.person.pk)
        self.assertEqual(entry, self.person)
