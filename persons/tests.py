from django.test import TestCase
from django.urls import reverse

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


class PersonsViewsTests(TestCase):

    def setUp(self):
        self.person = Person.objects.create(
            avatar='/static/images/cruel_galaxy_discordia_header.jpg',
            name='user', name_ru='юзер',
            profession='coder', profession_ru='кодер',
            about='description', about_ru='описание'
        )

    def test_project_view_en(self):
        response = self.client.get(reverse('project', args=['en']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.person.avatar.url)
        self.assertContains(response, self.person.name)
        self.assertContains(response, self.person.profession)
        self.assertContains(response, self.person.about)

    def test_project_view_ru(self):
        response = self.client.get(reverse('project', args=['ru']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.person.avatar.url)
        self.assertContains(response, self.person.name_ru)
        self.assertContains(response, self.person.profession_ru)
        self.assertContains(response, self.person.about_ru)
