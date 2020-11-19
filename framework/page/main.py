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

        # 如果是通用的step，在这里需要传入main.yml对应的路径
        path = "../page/main.yml"

        return ContactList(self.driver)
