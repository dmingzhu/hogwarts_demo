import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from web_wx_po_demo.core.base import base

"""
添加联系人页面：
定义服务
1.循环添加添加人，最后刷新页面
"""

class ContactAdd():
    def __init__(self, driver:webdriver):
        self.driver = driver

    def add_members(self):
        print("进入到add页面")

        index = 50
        acctid = 50
        phone_num = 13300000000
        user_list = []
        while acctid <= 50:
            #  填写username
            user = base().find(By.ID, "username")
            user.clear()
            user.send_keys("user_%d" % index)
            user_list.append("user_%d" % index)

            # 填写id
            acctid_ele = base().find(By.ID, "memberAdd_acctid")
            acctid_ele.clear()
            acctid_ele.send_keys(acctid)
            # 填写phone
            phone_ele = base().find(By.ID, "memberAdd_phone")
            phone_ele.clear()
            phone_ele.send_keys(phone_num)
            # 保存并继续添加
            next = base().find(By.LINK_TEXT, "保存并继续添加")
            next.click()
            time.sleep(3)
            index = index + 1
            acctid = acctid + 1
            phone_num = phone_num + 1
        self.driver.refresh()
        return user_list ,self.driver
