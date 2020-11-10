from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web_wx_po_demo.core.base_page import Base
from web_wx_po_demo.core.contact_page import ContactPage

"""
主页：
定义服务
1.跳转到添加成员入口
"""

class MenuIndex(Base):
    # 修改原有类中的_base_url变量
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def add_members_click(self):
        # add = self.driver.find_element(By.XPATH, '//*[@class="ww_indexImg ww_indexImg_AddMember"]')
        locator = (By.XPATH, '//*[@class="ww_indexImg ww_indexImg_AddMember"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        add = self.find(By.XPATH, '//*[@class="ww_indexImg ww_indexImg_AddMember"]')
        add.click()
        print("成功进入添加成员页面")
        return ContactPage(self.driver)










