import time

from selenium.webdriver.common.by import By

from web_wx_po_demo.core.base import base
from web_wx_po_demo.core.contact_add import ContactAdd

"""
主页：
定义服务
1.跳转到添加成员入口
"""

class MenuIndex(base):
    def __init__(self):
        self.driver = base().setup()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def index_service_add_members(self):
        # add = self.driver.find_element(By.XPATH, '//*[@class="ww_indexImg ww_indexImg_AddMember"]')
        locator = '//*[@class="ww_indexImg ww_indexImg_AddMember"]'
        add = base().find(By.XPATH, locator)
        time.sleep(1)
        add.click()
        print("111")

        return ContactAdd(self.driver).add_members()

if __name__ == "__main__":
    MenuIndex().index_service_add_members()









