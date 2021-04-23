from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from ..models import Person


class PersonsViewsTests(TestCase):
    """Case of testing persons views"""

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
        """Test: does project view return correct response
        with English language
        """
        settings.LANGUAGE_CODE = 'en'
        response = self.client.get(reverse('project'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project.html')

    def test_project_view_ru(self):
        """Test: does project view return correct response
        with Russian language
        """
        settings.LANGUAGE_CODE = 'ru'
        response = self.client.get(reverse('project'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project.html')
