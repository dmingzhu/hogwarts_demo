import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestAdd:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:62001"
        # caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "True"

        # 与appium 建立session链接
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(6)
        time.sleep(3)
    def teardown(self):
        self.driver.quit()

    def test_add_members(self):
        # 移动端的元素定位用mobileby
        self.driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()

        # 滑动页面，定位到添加成员元素，并点击进入添加成员页面
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                         'new UiScrollable(new UiSelector()'
                                         '.scrollable(true).instance(0))'
                                         '.scrollIntoView(new UiSelector()'
                                         '.text("添加成员").instance(0));').click()

        # 定位手动输入添加，并点击添加联系人
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        # 输入姓名
        name = "user_mobile_02"
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').clear()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(name)
        # ..表示父节点     上面这种方式是先找姓名所在的元素，再找这个元素的父节点，再找这个父节点下的目标子节点
        # '//*[@class="android.widget.RelativeLayout"]/android.widget.EditText[@text="必填"]'  直接写姓名的父节点，再从父节点往下找输入框

        # 选择性别
        self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        time.sleep(1)
        self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()

        # 输入手机号
        phone_num = 13310001002
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/fow"]').send_keys(phone_num)

        # 点击保存
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        # 打印当前页面布局
        # print(self.driver.page_source)
        # 接收到toast
        # result = self.driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
        result = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "添加成功")]').text
        assert result == "添加成功"


