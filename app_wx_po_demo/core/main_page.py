from appium.webdriver.common.mobileby import MobileBy

from app_wx_po_demo.core.base_page import BasePage
from app_wx_po_demo.core.contact_list_page import ContactList


class Main(BasePage):
    def goto_contact_list(self):
        print("跳转到通讯录页面")
        # 移动端的元素定位用mobileby
        self.find(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # self.driver.find_element()
        return ContactList(self.driver)
