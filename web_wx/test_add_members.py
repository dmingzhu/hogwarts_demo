import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.epic("企业微信")
@allure.story("添加成员")
class TestContacts:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_argument("--disable-gpu")
        # option.debugger_address = "127.0.0.1:9222"
        self.driver =webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_add(self):
        with allure.step("带cookie登录"):
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
            # cookie = self.driver.get_cookies()
            # print(cookie)

            # 存储cookie
            cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853130999886'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636037683, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1604496835'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'OKxfWXUcl7Ns6-jtJkO2ith5ZHIY_qUQXD38scrfVzqkKV2DNAefIpL2l5aoDLnlrYHOT3MqKUyC2zZz3A1BCwEgB-6asUn-SNH85ZoCse3x2SnGHPjmP01U02R59l8RnoEiHlN1ffdjXrqwPrR4CA4IbexcfniTCz11o0sb_fNpJIdChfI1vVDCpuSI0OobAr5slYLKEXskaMlYqEh6i7TcRmhhQPjbOsafwqCScA40i9MmZOkKyL-hW9JON92G4x85Ek5t4dD52Gu_M5OtEA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853130999886'}, {'domain': '.qq.com', 'expiry': 1604583251, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': 'work.weixin.qq.com', 'expiry': 1604614589, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '93dksnf'}, {'domain': '.qq.com', 'expiry': 1604669613, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.407376420.1604496836'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '9ZWDkDPgjmKpWf0fd4N2J7HFda_yXQ9FNcYrptiiqYIAibR9UWsUtsSciE97I8mC'}, {'domain': '.qq.com', 'expiry': 1612879210, 'httpOnly': False, 'name': 'sd_cookie_crttime', 'path': '/', 'secure': True, 'value': '1581343210829'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324945173189'}, {'domain': '.qq.com', 'expiry': 1911100721, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': True, 'value': '0_5f1d123885c85'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636032833, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': True, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'expiry': 1607175218, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1667655213, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2016739679.1581646814'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True, 'value': '7d66a85307626009a497d7b6349ed0624c19657526157d7f45890b2e198448e0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '31589051151991519'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a2358468'}, {'domain': '.qq.com', 'expiry': 1612879210, 'httpOnly': False, 'name': 'sd_userid', 'path': '/', 'secure': True, 'value': '23011581343210829'}, {'domain': '.qq.com', 'expiry': 1896612953, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': True, 'value': '253524a19564d7f9'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': True, 'value': '8338584744'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True, 'value': 'zBR53RLHNp'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': True, 'value': '7779940352'}]
            # 将cookie传值给浏览器,同时如果有expiry将其删除,删除key为expiry的这对键值对
            for cookie in cookies:
                if "expiry" in cookie.keys():
                    cookie.pop("expiry")
                self.driver.add_cookie(cookie)

            time.sleep(3)
            self.driver.refresh()
        with allure.step("打开通讯录>添加成员"):
        # 点击添加成员
            add = self.driver.find_element(By.XPATH ,'//*[@class="ww_indexImg ww_indexImg_AddMember"]')
            time.sleep(1)
            add.click()

        with allure.step("填写姓名，账号，手机号保存"):
            #进入添加页面
            index = 10
            print(index)
            acctid = 10
            phone_num = 13300000000

            while  acctid <= 30:
                #  填写username
                user = self.driver.find_element_by_id("username")
                user.clear()
                user.send_keys("user_%d"%index)
                # 填写id
                acctid_ele = self.driver.find_element_by_id("memberAdd_acctid")
                acctid_ele.clear()
                acctid_ele.send_keys(acctid)
                # 填写phone
                phone_ele = self.driver.find_element_by_id("memberAdd_phone")
                phone_ele.clear()
                phone_ele.send_keys(phone_num)
                # 保存并继续添加
                next = self.driver.find_element_by_link_text("保存并继续添加")
                next.click()
                time.sleep(3)
                index = index + 1
                acctid = acctid + 1
                phone_num = phone_num + 1

        with allure.step("填写完成刷新页面"):
            self.driver.refresh()
            time.sleep(3)
            try:
                self.driver.save_screenshot("./picture/add_members.png")
                allure.attach.file("./picture/add_members.png", attachment_type=allure.attachment_type.PNG)
            except Exception:
                raise Exception

            else:
                print("截图成功")

