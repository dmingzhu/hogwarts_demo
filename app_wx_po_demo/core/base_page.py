import logging

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.remote.mobile import Mobile

"""
定义一个基类，
1.初始化driver,完成对driver的复用
2.封装find_element
3.封装滚动查找
4.封装显示等待
5.添加日志
"""

class BasePage:
    # 添加日志
    # logging.basicConfig(level=logging.INFO,
    #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #                     datefmt='%a, %d %b %Y %H:%M:%S',
    #                     filename='../log/myapp.log',
    #                     filemode='w')

    # basepage初始化了一个driver
    def __init__(self, driver:webdriver=None):
            self.driver = driver

    def find(self, by, locator):
        logging.info("find:")
        logging.info(by)
        logging.info(locator)
        return self.driver.find_element(by, locator)

    def find_by_scroll(self, text):
        logging.info("find_by_scroll")
        logging.info(text)


        return self.find(MobileBy.ANDROID_UIAUTOMATOR,
                  'new UiScrollable(new UiSelector()'
                  '.scrollable(true).instance(0))'
                  '.scrollIntoView(new UiSelector()'
                  f'.text("{text}").instance(0));').click()

    def get_toast_text(self):
        logging.info("get toast:")
        toast_text = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(toast_text)
        return toast_text