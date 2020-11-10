import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web_wx_po_demo.core.base_page import Base

"""
添加联系人页面：
定义服务
1.循环添加添加人，最后刷新页面
"""

class ContactPage(Base):
    def add_members(self):
        print("进入到add页面")

        index = 50
        acctid = 50
        phone_num = 13300000000
        user_list = []
        while acctid <= 50:
            #  填写username
            user = self.find(By.ID, "username")
            user.clear()
            user.send_keys("user_%d" % index)
            user_list.append("user_%d" % index)

            # 填写id
            acctid_ele = self.find(By.ID, "memberAdd_acctid")
            acctid_ele.clear()
            acctid_ele.send_keys(acctid)
            # 填写phone
            phone_ele = self.find(By.ID, "memberAdd_phone")
            phone_ele.clear()
            phone_ele.send_keys(phone_num)
            # 保存并继续添加
            next = self.find(By.LINK_TEXT, "保存并继续添加")
            next.click()
            # time.sleep(3)
            index = index + 1
            acctid = acctid + 1
            phone_num = phone_num + 1
        self.driver.refresh()
        return user_list

    # 获取最后一页的最后一个用户姓名
    # 先判断，当前页码是不是最大值   先定位页码，再比较当前页码和最大页码值
    # 若不是则翻到最后一页
    # 若是,则定位到最后一个用户姓名,并获取title属性值
    def get_members(self):
        print("获取实际结果")
        # time.sleep(2)
        page_text = self.find(By.XPATH, '//*[@class="ww_pageNav_info_text"]').text
        print(page_text)

        # 拆分页码值，获取当前的页码和最大页码
        page_text_list = page_text.split("/")
        print(page_text_list)
        current_page_num = int(page_text_list[0])
        max_page_num = int(page_text_list[1])
        # 循环判断页码大小，翻页
        while current_page_num < max_page_num:
            self.find(By.XPATH, '//*[@class="ww_pageNav_info_arrowWrap js_next_page"]').click()
            current_page_num += 1

        dest_username_locator = '//*[@class="member_colRight_memberTable ww_table js_ww_table"]//tr[2]/td[2]'
        actual_username_dest = self.find(By.XPATH, dest_username_locator).get_attribute("title")
        print(actual_username_dest)
        return actual_username_dest

if __name__ == "__main__":
    aa = ContactPage()
    aa.get_members()