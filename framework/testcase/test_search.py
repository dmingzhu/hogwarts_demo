import pytest
import yaml

from framework.page.app import App


class TestCase:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    def test_search(self):
        self.main.goto_contact_list().search()
        # self.main.step()

    def teardown_class(self):
        self.app.stop()


