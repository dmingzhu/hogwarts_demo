# -*- coding:utf-8 -*-
# @time    :2020/11/4 21:35
# @Author  :dmingzhu
# @dmingzhu:test_add_member.py
import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWX:
    def setup(self):
        # 复用浏览器
        option = Options()
        option.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options = option)
        self.driver = webdriver.Chrome()



    def teardown(self):
        self.driver.quit()

    def test_get_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 1.先用复用浏览器的方式拿到浏览器当前的cookie
        # 2.再将将这个cookie存入变量，遍历的方式将独立的单个字典传入浏览其中
        # 3.去掉浏览器的选项，开始执行用例
        # cookie = self.driver.get_cookies()
        cookie_list = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853130999886'}, {'domain': '.qq.com', 'expiry': 1604502069, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'aem2VEYBm34HYkWcdR5Sukuzv75rmcmRKArYlzbkY4j-egiOa2lgnV7SXp_gaFhzhdTjUWI05sehJhDEGL1W2jQSr6-SzsVEJiS_h6oi4vw6amYRci97-aCZHshkr4E4-kyMktXgqY-2rap-_liwEO26heEbDUmu72J2-eESGB_4J9U2qDOxb1cZ0qfqqVFH9gri7_sC5RgAiZWrdTx4fppgRhy8zbaKLxjYf4bHStExiUeJpZDtM4trOlU2rd6Atmb_sWCkeMigXt2T5w4l5Q'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636037683, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1604496835'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853130999886'}, {'domain': '.work.weixin.qq.com', 'expiry': 1604528369, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': True, 'value': '5dludh5'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '9ZWDkDPgjmKpWf0fd4N2J4hICNUk573v0ORh8OHoQi4TmtE9l3p8sRZpaXmkkC8i'}, {'domain': '.qq.com', 'expiry': 1604588418, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.407376420.1604496836'}, {'domain': 'work.weixin.qq.com', 'expiry': 1604528369, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '5dludh5'}, {'domain': '.qq.com', 'expiry': 1612879210, 'httpOnly': False, 'name': 'sd_cookie_crttime', 'path': '/', 'secure': True, 'value': '1581343210829'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324945173189'}, {'domain': '.qq.com', 'expiry': 1911100721, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': True, 'value': '0_5f1d123885c85'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636032833, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': True, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1607094028, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1667574018, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2016739679.1581646814'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True, 'value': '7d66a85307626009a497d7b6349ed0624c19657526157d7f45890b2e198448e0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '31589051153582960'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5738287'}, {'domain': '.qq.com', 'expiry': 1612879210, 'httpOnly': False, 'name': 'sd_userid', 'path': '/', 'secure': True, 'value': '23011581343210829'}, {'domain': '.qq.com', 'expiry': 1896612953, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': True, 'value': '253524a19564d7f9'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': True, 'value': '8338584744'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True, 'value': 'zBR53RLHNp'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': True, 'value': '7779940352'}]
        # print(cookie)
        # 将获取到的cookie传入到当前的浏览器中
        for cookie in cookie_list:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)
        #
        self.driver.refresh()
        time.sleep(2)

    def test_cookie_db(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        # 数据库时以key和value的形式存储的

        # 创建一个cookies,db文件
        db = shelve.open("cookies")
        # 将复用获取到cookies存储到db对用的文件中
        # db["cookies"] =  [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853130999886'}, {'domain': '.qq.com', 'expiry': 1604502069, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'aem2VEYBm34HYkWcdR5Sukuzv75rmcmRKArYlzbkY4j-egiOa2lgnV7SXp_gaFhzhdTjUWI05sehJhDEGL1W2jQSr6-SzsVEJiS_h6oi4vw6amYRci97-aCZHshkr4E4-kyMktXgqY-2rap-_liwEO26heEbDUmu72J2-eESGB_4J9U2qDOxb1cZ0qfqqVFH9gri7_sC5RgAiZWrdTx4fppgRhy8zbaKLxjYf4bHStExiUeJpZDtM4trOlU2rd6Atmb_sWCkeMigXt2T5w4l5Q'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636037683, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1604496835'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853130999886'}, {'domain': '.work.weixin.qq.com', 'expiry': 1604528369, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': True, 'value': '5dludh5'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '9ZWDkDPgjmKpWf0fd4N2J4hICNUk573v0ORh8OHoQi4TmtE9l3p8sRZpaXmkkC8i'}, {'domain': '.qq.com', 'expiry': 1604588418, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.407376420.1604496836'}, {'domain': 'work.weixin.qq.com', 'expiry': 1604528369, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '5dludh5'}, {'domain': '.qq.com', 'expiry': 1612879210, 'httpOnly': False, 'name': 'sd_cookie_crttime', 'path': '/', 'secure': True, 'value': '1581343210829'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324945173189'}, {'domain': '.qq.com', 'expiry': 1911100721, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': True, 'value': '0_5f1d123885c85'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636032833, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': True, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1607094028, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1667574018, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2016739679.1581646814'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True, 'value': '7d66a85307626009a497d7b6349ed0624c19657526157d7f45890b2e198448e0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '31589051153582960'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5738287'}, {'domain': '.qq.com', 'expiry': 1612879210, 'httpOnly': False, 'name': 'sd_userid', 'path': '/', 'secure': True, 'value': '23011581343210829'}, {'domain': '.qq.com', 'expiry': 1896612953, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': True, 'value': '253524a19564d7f9'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': True, 'value': '8338584744'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True, 'value': 'zBR53RLHNp'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': True, 'value': '7779940352'}]

        # 从数据库中去除cookie,添加到浏览器
        cookie_list = db["cookies"]
        db.close()

        for cookie in cookie_list:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        time.sleep(2)



    def test_add(self):
        # 点击添加成员
        self.driver.find_element_by_class_name("index_service_cnt_item_title").click()
        time.sleep(3)