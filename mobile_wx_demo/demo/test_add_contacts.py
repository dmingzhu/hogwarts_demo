import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "127.0.0.1:7555"
caps["appPackage"] = "com.tencent.wework"
caps["appActivity"] = ".launch.WwMainActivity"
caps["noReset"] = "True"

# 与appium 建立session链接
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(6)
# time.sleep(3)
# 移动端的元素定位用mobileby
driver.find_element(MobileBy.XPATH,'//*[@text="通讯录"]').click()

# 滑动页面，定位到添加成员元素，并点击进入添加成员页面
driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("添加成员").instance(0));').click()

# 定位手动输入添加，并点击添加联系人
driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
# 输入姓名
name = "user_mobile_02"
driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').clear()
driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(name)

# 选择性别
driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
time.sleep(1)
driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()

# 输入手机号
phone_num = 13310001001
driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/fow"]').send_keys(phone_num)

# 点击保存
driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()

time.sleep(2)
# 接收到toast
result = driver.find_element(MobileBy.XPATH, '//*[@class="android.widget.Toast"]').text
if result == "添加成功":
    print("添加测试通过")
else:
    print("添加测试不通过")


driver.quit()

