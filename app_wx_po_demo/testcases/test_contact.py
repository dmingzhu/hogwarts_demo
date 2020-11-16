from app_wx_po_demo.core.app import App
from app_wx_po_demo.core.base_page import BasePage


class TestCase():
    # 在类级别的装置中定义一个app
    def setup_class(self):
        self.app = App()

    # 在类方法级别的装置中定义一个main
    def setup(self):
        self.main = self.app.start().goto_main()

    # 测试添加
    def test_add(self):
        # 链式调用
        name = "user_mobile_02"
        phone_num = 13310001002
        result = self.main.goto_contact_list().goto_add().goto_add_by_manual().add_members(name, phone_num)
        assert result == "添加成功"

    # 测试删除
    def test_del(self):
        # 返回删除后的结果
        name = "user_mobile_02"
        result = self.main.goto_contact_list().goto_delete_by_search(name)
        assert result == "无搜索结果"

    def teardown_class(self):
        self.app.stop()