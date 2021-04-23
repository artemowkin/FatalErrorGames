from django.test import TestCase

from ..models import Person


class PersonModelTests(TestCase):
    """Case of testing person model"""

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

    def test_created_person_fields_valid(self):
        """Test: are created person fields valid"""
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
