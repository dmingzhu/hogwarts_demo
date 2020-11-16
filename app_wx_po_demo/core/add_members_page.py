import time

from appium.webdriver.common.mobileby import MobileBy

from app_wx_po_demo.core.base_page import BasePage


class AddMembers(BasePage):
    def add_members(self, name, phone_num):
        # 输入姓名

        self.find(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').clear()
        self.find(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
            name)
        # ..表示父节点     上面这种方式是先找姓名所在的元素，再找这个元素的父节点，再找这个父节点下的目标子节点
        # '//*[@class="android.widget.RelativeLayout"]/android.widget.EditText[@text="必填"]'  直接写姓名的父节点，再从父节点往下找输入框

        # 选择性别
        self.find(MobileBy.XPATH, '//*[@text="男"]').click()
        time.sleep(1)
        self.find(MobileBy.XPATH, '//*[@text="男"]').click()

        # 输入手机号

        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/fow"]').send_keys(phone_num)

        # 点击保存
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()
        # result = self.find(MobileBy.XPATH, '//*[contains(@text, "添加成功")]').text
        result = self.get_toast_text()
        return result