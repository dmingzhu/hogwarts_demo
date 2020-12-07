from wework_api_framework.tag import TagApi


class TestTag:
    def setup(self):
        self.api = TagApi()

    def test_add_corp_tag(self):
        add_data = {
                "group_id": "GROUP_ID",
                "group_name": "GROUP_NAME",
                "order": 1,
                "tag": [{
                    "name": "TAG_NAME_1",
                    "order": 1
                },
                    {
                        "name": "TAG_NAME_2",
                        "order": 2
                    }
                ]
            }
        self.api.add_corp_tag(add_data)


