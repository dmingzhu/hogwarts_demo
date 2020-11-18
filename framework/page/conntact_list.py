from appium.webdriver.common.mobileby import MobileBy

from framework.page.base_page import BasePage


class ContactList(BasePage):
    def goto_search(self):
        self.find(MobileBy.ID,"com.tencent.wework:id/i6n").click()
        self.find(MobileBy.XPATH, '//*[@text="搜索"]').send_keys("user_mobile_04")
        return True
