from wework_api_framework.tag import TagApi


class TestTag:
    def setup(self):
        self.api = TagApi()

    def test_creat_tag(self):
        creat_data = {
            "tagname": "tag_UI_14",
            "tagid": 14
        }
        self.api.creat_tag(creat_data)

    def test_get_taglist(self):
        self.api.get_tag_list()

