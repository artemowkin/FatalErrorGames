import time

from .base import FunctionalTest
from persons.models import Person


class PersonsFunctionalTest(FunctionalTest):
    """Functional test for persons"""

    def setUp(self):
        super().setUp()
        self.person = Person.objects.create(
            avatar="person.jpg", name="Steve", profession="developer",
            about="Some text about"
        )

    def test_concrete_game_page(self):
        # Get a project page
        self.browser.get(self.live_server_url + '/project/')
        time.sleep(0.5)

        # Check has menu bar project link
        project_link = self.browser.find_element_by_class_name("active_link")
        self.assertEqual(project_link.text, "Project")

        # Check has project article person information
        person = self.browser.find_element_by_class_name('person')
        person_name = person.find_element_by_tag_name('h3')
        person_profession = person.find_element_by_tag_name('small')
        person_about = person.find_element_by_tag_name('p')
        self.assertEqual(person_name.text, self.person.name)
        self.assertEqual(person_profession.text, self.person.profession)
        self.assertEqual(person_about.text, self.person.about)
