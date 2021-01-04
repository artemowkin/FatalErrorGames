from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from .models import Person
import services.common as services_common


class PersonModelTests(TestCase):

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


class PersonServicesTests(TestCase):

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

    def test_get_all_model_entries(self):
        all_persons = services_common.get_all_model_entries(Person)
        self.assertEqual(len(all_persons), 1)
        self.assertEqual(all_persons[0], self.person)


class PersonsViewsTests(TestCase):

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

    def test_project_view_en(self):
        settings.LANGUAGE_CODE = 'en'
        response = self.client.get(reverse('project'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.person.avatar.url)
        self.assertContains(response, self.person.name)
        self.assertContains(response, self.person.profession)
        self.assertContains(response, self.person.about)

    def test_project_view_ru(self):
        settings.LANGUAGE_CODE = 'ru'
        response = self.client.get(reverse('project'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.person.avatar.url)
        self.assertContains(response, self.person.name_ru)
        self.assertContains(response, self.person.profession_ru)
        self.assertContains(response, self.person.about_ru)
