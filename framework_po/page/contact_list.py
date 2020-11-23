import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from framework_po.page.base_page import BasePage


class ContactList(BasePage):
    def search(self, value):
        self._params["value"] = value
        path = "../page/contact_list.yml"
        self.steps(path)
        # self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/i6n"]').click()
        # self.find(MobileBy.XPATH, '//*[@text="搜索"]').send_keys("user_mobile_04")

        return True
