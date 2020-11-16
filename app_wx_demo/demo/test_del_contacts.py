import time

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

class TestDel:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        # caps["deviceName"] = "127.0.0.1:7555"
        caps["deviceName"] = "127.0.0.1:62001"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "True"

        # 与appium 建立session链接
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(6)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_del(self):
        # 移动端的元素定位用mobileby,定位到通讯录
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()
        # 滑动到通讯录底部,定位到要删除的对象,并点击
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                         'new UiScrollable(new UiSelector()'
                                         '.scrollable(true).instance(0))'
                                         '.scrollIntoView(new UiSelector()'
                                         '.text("user_mobile_01").instance(0));').click()
        time.sleep(1)
        # 定位目标姓名，并点击
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/i6d"]').click()
        time.sleep(2)
        # 定位编辑成员，并点击
        self.driver.find_element(MobileBy.XPATH,'//*[@text="编辑成员"]').click()
        # 定位删除成员，并单击
        self.driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        # time.sleep(1
        # 定位到这个弹窗确定
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/blx"]').click()
        time.sleep(1)

    def test_del_by_search(self):
        # 移动端的元素定位用mobileby,定位到通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        time.sleep(2)
        # 定位到搜索，并点击
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/i6n"]').click()
        # 输入目标姓名，并点击搜索
        name = "user_mobile_02"
        self.driver.find_element(MobileBy.XPATH, '//*[@text="搜索"]').send_keys(name)
        time.sleep(2)
        self.driver.find_element(MobileBy.XPATH,
                                 '//*[@resource-id="com.tencent.wework:id/gqx"]/android.widget.RelativeLayout[@index="1"]').click()

        # 定位到更多
        time.sleep(1)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/i6d").click()
        # 定位编辑成员，并点击
        self.driver.find_element(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        # 定位删除成员，并单击
        self.driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        # time.sleep(1
        # 定位到这个弹窗确定
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/blx"]').click()
        time.sleep(1)

        # 判断是否删除成功
        result = self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/ccl').text
        assert result == "无搜索结果"