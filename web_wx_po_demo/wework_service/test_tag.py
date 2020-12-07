from web_wx_po_demo.wework_service.tag import Tag


class TestTag:
    # 测试用例初始化，火球token
    def setup(self):
        self.tag = Tag()
        self.api = self.tag.get_token()

    def test_add(self):
        pass
