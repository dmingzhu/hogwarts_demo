from appium.webdriver.common.mobileby import MobileBy

from app_wx_po_demo.core.add_members_page import  AddMembers
from app_wx_po_demo.core.base_page import BasePage


class Add(BasePage):
    def goto_add_by_manual(self):
        print("跳转到手动添加成员页面")
        # 定位手动输入添加，并点击添加联系人
        self.find(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return AddMembers(self.driver)
