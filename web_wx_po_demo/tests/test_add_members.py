from selenium.webdriver.common.by import By

from web_wx_po_demo.core.base import base
from web_wx_po_demo.core.menu_index import MenuIndex


class TestAdd:
    """
    根据当前联系人列表中是否存在已添加的联系人姓名,来判断是否添加成功
    1.调用业务代码，获取添加的联系人姓名
    2.判断当前列表联系人是否包含添加的名称
    3.断言包含为true
    """
    def test_add(self):
        # 添加的用户姓名
        result = MenuIndex().index_service_add_members()
        expect_username = result[0]
        # 接收从业务中返回的浏览器
        self.driver = result[1]

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

        # 获取最后一页的最后一个用户姓名
        # 先判断，当前页码是不是最大值   先定位页码，再比较当前页码和最大页码值
        # 若不是则翻到最后一页
        # 若是,则定位到最后一个用户姓名,并获取title属性值,再和逾期结果比较，断言
        page_locator = '//*[@class="ww_pageNav_info_text"]'
        page_text = base().find(By.XPATH, page_locator).text
        print(page_text)

        # 拆分页码值，获取当前的页码和最大页码
        page_text_list = page_text.split("/")
        print(page_text_list)
        current_page_num = int(page_text_list[0])
        max_page_num = int(page_text_list[1])
        # 循环判断页码大小，翻页
        while current_page_num < max_page_num:
            base().find(By.XPATH, '//*[@class="ww_pageNav_info_arrowWrap js_next_page"]').click()
            current_page_num += 1

        dest_username_locator = '//*[@class="member_colRight_memberTable ww_table js_ww_table"]//tr[2]/td[2]'
        actual_username_dest = base().find(By.XPATH, dest_username_locator).get_attribute("title")
        print(actual_username_dest)
        if actual_username_dest in expect_username:
            assert True
        else:
            assert False
