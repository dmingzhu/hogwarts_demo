"""
定义app的基本操作
"""
from appium import webdriver

from app_wx_po_demo.core.base_page import BasePage

"""
对app常用的方法，进行封装
1.启动
2.重启
3.停止
4.跳转到主页
"""
class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["noRest"] = True
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(3)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def goto_main(self):
        return Main(self.driver)