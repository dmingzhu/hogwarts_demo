from web_wx_po_demo.wework_service.tag import Tag


class TestTag:
    # 测试用例初始化，火球token
    def setup(self):
        self.tag = Tag()

    def test_add(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        add_data = {
            "group_id": "GROUP_1",
            "group_name": "GROUP_NAME_1",
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
        r = self.tag.add(url=url, add_data=add_data)
        print(r)
