import pytest
import yaml

from framework.page.app import App


class TestCase:
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.main = self.app.start().goto_main()

    @pytest.mark.parametrize("value", yaml.safe_load(open("./contact_list_search.yml", encoding="utf-8")))
    def test_search(self, value):
        self.main.goto_contact_list().search(value)
        # self.main.step()

    def teardown_class(self):
        self.app.stop()


