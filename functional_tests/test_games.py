import time

from .base import FunctionalTest
from games.models import Game


class GamesFunctionalTest(FunctionalTest):
    """Functional test for games"""

    def setUp(self):
        super().setUp()
        self.game = Game.objects.create(
            title="Some game", slug="some-game", preview="preview.jpg",
            short_description="some short description",
            description="some description",
            video="https://www.youtube.com/watch?v=w-stfAxYzKw"
        )

    def test_concrete_game_page(self):
        # Get a concrete game page
        self.browser.get(self.live_server_url + '/games/some-game/')
        time.sleep(0.5)

        # Check has menu bar game link
        game_link = self.browser.find_element_by_class_name("active_link")
        self.assertEqual(game_link.text, self.game.title)

        # Check has game article game title
        game_title = self.browser.find_element_by_class_name("game_title")
        self.assertEqual(game_title.text, self.game.title)

        # Check has game article game short descritpion
        game_short_description = self.browser.find_element_by_class_name(
            "game_short_description"
        )
        self.assertEqual(
            game_short_description.text, self.game.short_description
        )

        # Check has game article game description
        game_description = self.browser.find_element_by_class_name(
            "game_description"
        )
        self.assertEqual(game_description.text, self.game.description)
