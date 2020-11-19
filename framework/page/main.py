import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy

from framework.page.base_page import BasePage
from framework.page.contact_list import ContactList


class Main(BasePage):
    def goto_contact_list(self):
        print("跳转到通讯录页面")
        # 在main中调用步骤
        self.step_main()
        # 移动端的元素定位用mobileby
        # self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # self.driver.find_element()
        return ContactList(self.driver)
