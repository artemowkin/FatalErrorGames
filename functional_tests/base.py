from selenium import webdriver
from django.test import LiveServerTestCase


class FunctionalTest(LiveServerTestCase):
    """Base class for functional tests"""

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.close()
