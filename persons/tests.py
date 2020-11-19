from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from .models import Person
from .services import PersonService
from langs.models import Language


class PersonModelTests(TestCase):

    def setUp(self):
        self.lang = Language.objects.create(code='en')
        self.person = Person.objects.create(
            avatar='/static/images/cruel_galaxy_discordia_header.jpg',
            name='user',
            profession='coder',
            about='description',
            language=self.lang
        )

    def test_fields(self):
        self.assertEqual(
            self.person.avatar.url,
            '/media/static/images/cruel_galaxy_discordia_header.jpg'
        )
        self.assertEqual(self.person.name, 'user')
        self.assertEqual(self.person.profession, 'coder')
        self.assertEqual(self.person.about, 'description')
        self.assertEqual(self.person.language, self.lang)


class PersonServiceTests(TestCase):

    def setUp(self):
        self.lang = Language.objects.create(code='en')
        self.person = Person.objects.create(
            avatar='/static/images/cruel_galaxy_discordia_header.jpg',
            name='user',
            profession='coder',
            about='description',
            language=self.lang,
        )
        self.service = PersonService()

    def test_get_all(self):
        all_persons = self.service.get_all()
        self.assertEqual(len(all_persons), 1)
        self.assertEqual(all_persons[0], self.person)

    def test_get_all_ru(self):
        all_persons = self.service.get_all('ru')
        self.assertEqual(len(all_persons), 1)
        self.assertEqual(all_persons[0], self.person)

    def test_get_all_ru_with_ru_person(self):
        lang_ru = Language.objects.create(code='ru')
        person_ru = Person.objects.create(
            avatar='/static/images/cruel_galaxy_discordia_header.jpg',
            name='Пользователь',
            profession='Программист',
            about='Описание',
            language=lang_ru,
        )
        all_persons = self.service.get_all(lang_ru.code)
        self.assertEqual(len(all_persons), 1)
        self.assertEqual(all_persons[0], person_ru)

    def test_get_concrete(self):
        entry = self.service.get_concrete(self.person.pk)
        self.assertEqual(entry, self.person)

    def test_get_concrete_ru(self):
        entry = self.service.get_concrete(self.person.pk, 'ru')
        self.assertEqual(entry, self.person)

    def test_get_concrete_ru_with_person_ru(self):
        lang_ru = Language.objects.create(code='ru')
        person_ru = Person.objects.create(
            avatar='/static/images/cruel_galaxy_discordia_header.jpg',
            name='Пользователь',
            profession='Программист',
            about='Описание',
            language=lang_ru,
        )
        entry = self.service.get_concrete(person_ru.pk, lang_ru.code)
        self.assertEqual(entry, person_ru)


class PersonsViewsTests(TestCase):

    def setUp(self):
        self.lang = Language.objects.create(code='en')
        self.lang_ru = Language.objects.create(code='ru')
        self.person = Person.objects.create(
            avatar='/static/images/cruel_galaxy_discordia_header.jpg',
            name='user',
            profession='coder',
            about='description',
            language=self.lang,
        )
        self.person_ru = Person.objects.create(
            avatar='/static/images/cruel_galaxy_discordia_header.jpg',
            name='Пользователь',
            profession='Программист',
            about='Описание',
            language=self.lang_ru,
        )

    def test_project_view_en(self):
        settings.LANGUAGE_CODE = self.lang.code
        response = self.client.get(reverse('project'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.person.avatar.url)
        self.assertContains(response, self.person.name)
        self.assertContains(response, self.person.profession)
        self.assertContains(response, self.person.about)

    def test_project_view_ru(self):
        settings.LANGUAGE_CODE = self.lang_ru.code
        response = self.client.get(reverse('project'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.person_ru.avatar.url)
        self.assertContains(response, self.person_ru.name)
        self.assertContains(response, self.person_ru.profession)
        self.assertContains(response, self.person_ru.about)
