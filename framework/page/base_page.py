
"""
把框架中公共的方法抽离出来，方便调用
"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class BasePage:

    # basepage初始化了一个driver
    def __init__(self, driver:webdriver=None):
            self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_by_scroll(self, text):
        return self.find(MobileBy.ANDROID_UIAUTOMATOR,
                  'new UiScrollable(new UiSelector()'
                  '.scrollable(true).instance(0))'
                  '.scrollIntoView(new UiSelector()'
                  f'.text("{text}").instance(0));').click()

    def get_toast_text(self):
        toast_text = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return toast_text
