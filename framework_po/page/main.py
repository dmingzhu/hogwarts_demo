import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy

from framework_po.page.base_page import BasePage
from framework_po.page.contact_list import ContactList


class Main(BasePage):
    def goto_contact_list(self):
        print("跳转到通讯录页面")
        # 在main中调用步骤
        path = "../page/main.yml"
        self.steps(path)

        # 如果是通用的step，在这里需要传入main.yml对应的路径
        return ContactList(self.driver)
