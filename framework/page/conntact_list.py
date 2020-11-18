from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver
from framework.page.base_page import BasePage


class ContactList(BasePage):
    def search(self):
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/i6n"]').click()
        self.find(MobileBy.XPATH, '//*[@text="搜索"]').send_keys("user_mobile_04")
        return True
