
"""
把框架中公共的方法抽离出来，方便调用
"""
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver:WebDriver = None):
        self.driver = driver


    def find(self, by, locator):
        return self.driver.find_element(by, locator)
