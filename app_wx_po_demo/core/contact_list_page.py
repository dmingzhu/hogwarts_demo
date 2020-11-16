import time

from appium.webdriver.common.mobileby import MobileBy

from app_wx_po_demo.core.add_page import Add
from app_wx_po_demo.core.base_page import BasePage


class ContactList(BasePage):
    def goto_add(self):
        print("跳转到添加选择页面")
        # 滑动页面，定位到添加成员元素，并点击进入添加成员页面
        text = "添加成员"
        self.find_by_scroll(text)
        # self.find(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector()'
        #                          '.scrollable(true).instance(0))'
        #                          '.scrollIntoView(new UiSelector()'
        #                          '.text("添加成员").instance(0));').click()

        return Add(self.driver)

    def goto_delete_by_search(self, name):
        print("跳转到搜索页")
        # 定位到搜索，并点击
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/i6n"]').click()
        # 输入目标姓名，并点击搜索

        self.find(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        time.sleep(2)
        self.find(MobileBy.XPATH,
                                 '//*[@resource-id="com.tencent.wework:id/gqx"]/android.widget.RelativeLayout[@index="1"]').click()

        # 定位到更多
        time.sleep(1)
        self.find(MobileBy.ID, "com.tencent.wework:id/i6d").click()
        # 定位编辑成员，并点击
        self.find(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        # 定位删除成员，并单击
        self.find(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        # time.sleep(1
        # 定位到这个弹窗确定
        self.find(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/blx"]').click()
        time.sleep(1)

        # 判断是否删除成功
        result = self.find(MobileBy.ID, 'com.tencent.wework:id/ccl').text
        return result
