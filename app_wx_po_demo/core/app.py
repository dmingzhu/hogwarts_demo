from appium import webdriver

from app_wx_po_demo.core.base_page import BasePage
from app_wx_po_demo.core.main_page import Main

"""
声明一个app对象，继承BasePage（自带driver属性）
方法：
1.启动
2.重启
3.停止
4.进入主页
"""
class App(BasePage):
    """定义app的启动方法"""
    def start(self):
        if self.driver == None:
            print("初始化一个driver")
            caps = {}
            caps["platformName"] = "Android"
            # caps["deviceName"] = "127.0.0.1:62001"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.WwMainActivity"
            caps["noReset"] = True

            # 与appium服务器建立连接
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

            self.driver.implicitly_wait(6)
        else:
            print("driver不为none,直接启动")
            self.driver.launch_app()
            # 也可以直接启动
            # self.driver.start_activity("com.tencent.wework",".launch.LaunchSplashActivity")

        return self

    """定义app的重启方法"""
    def restart(self):
        pass

    """定义app的停止方法"""
    def stop(self):
        self.driver.quit()

    """定义app进入主页的方法"""
    def goto_main(self):
        return Main(self.driver)