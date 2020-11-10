from selenium import webdriver
from selenium.webdriver.common.by import By


class Base(object):
    """
    定义基类
    1.初始化浏览器，如果浏览器 不为空，就沿用之前的.这样不用其他类再调用的过程中都去初始化一遍，继承了这个类就有这个driver
    2.初始化get url
    """
    _base_url = ""
    def __init__(self, driver = None):

        if driver == None:
            opt = webdriver.ChromeOptions()
            # opt.add_argument("--disable-gpu")
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(6)
        else:
            self.driver = driver

        if self._base_url != "":
            self.driver.get(self._base_url)


    # 封装find_element
    def find(self, by, locator):
        return self.driver.find_element(by, locator)


