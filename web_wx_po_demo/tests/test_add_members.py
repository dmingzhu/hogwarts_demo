import time

from selenium.webdriver.common.by import By

from web_wx_po_demo.core.base_page import Base
from web_wx_po_demo.core.menu_index_page import MenuIndex


class TestAdd:
    """
    根据当前联系人列表中是否存在已添加的联系人姓名,来判断是否添加成功
    1.调用业务代码，获取添加的联系人姓名
    2.判断当前列表联系人是否包含添加的名称
    3.断言包含为true
    """
    def setup(self):
        self.index = MenuIndex()

    def test_add(self):
        # 实际添加的用户姓名
        # expect_username = self.index.add_members_click().add_members()

        # 接收从业务中返回的浏览器
        # 获取当前页面上的添加成功的第一个用户姓名
        # current_username_locator = '//*[@class="member_colRight_memberTable ww_table js_ww_table"]//tr[@data-type="member"][2]/td[@class="member_colRight_memberTable_td"][1]'
        # by = By.XPATH
        # actual_username = base().find(by, current_username_locator).get_attribute("title")
        # print(actual_username)
        # if actual_username in expect_username:
        #     assert True
        #     print("测试通过")
        # else:
        #     assert False

        # 再和预期结果比较，断言
        result = self.index.add_members_click()
        user_ist = result.add_members()

        actual_username_dest = result.get_members()
        print(actual_username_dest)
        if actual_username_dest in user_ist:
            assert True
        else:
            assert False
