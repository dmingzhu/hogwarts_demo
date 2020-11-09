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
        option.debugger_address = "127.0.0.1:9222"
        self.driver =webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_add(self):

        """
        # 存储cookie，利用cookie进行浏览器的复用
        """
        # with allure.step("带cookie登录"):
        #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        #     # cookie = self.driver.get_cookies()
        #     # print(cookie)
        #
        #
        #     # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5566166'}, {'domain': '.qq.com', 'expiry': 1604885495, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': '9ZWDkDPgjmKpWf0fd4N2J2X-PlCtyKqaNBfOzHKpnFF6dlrbxiBur_nE9e-hrezl'}, {'domain': '.qq.com', 'expiry': 1604971887, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1573432439.1604885435'}, {'domain': 'work.weixin.qq.com', 'expiry': 1604916956, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '326as75'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1604480499'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853130999886'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853130999886'}, {'domain': '.work.weixin.qq.com', 'expiry': 1607477491, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1667957487, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.764296164.1604474985'}, {'domain': '.qq.com', 'expiry': 1884311773, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': 'd07ccc8f5ed30919'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636010810, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'qm_verifyimagesession', 'path': '/', 'secure': False, 'value': 'h01ed295e957db2b7553adaadcc3dade5200f9aa88fab6de3aaee664698def479a408f5151a4b33d1f5'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'qm_authimgs_id', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'skey', 'path': '/', 'secure': False, 'value': '@GgNI4FJ3W'}, {'domain': '.qq.com', 'expiry': 1819960748, 'httpOnly': False, 'name': 'pt_sms_phone', 'path': '/', 'secure': False, 'value': '186******53'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'uin', 'path': '/', 'secure': False, 'value': 'o1923675960'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '14914783731611721'}, {'domain': '.qq.com', 'expiry': 1606552747, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1923675960'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'nLwgHNq31Fmv7pajDKWchCL7PkZr5x7GtqZPKlrLgXtaoYckaEkDS-Yq8Ta4FK7fditLXNhYJ1ai4IunmhC1fnkYmKA0rcFee2LNuyog-2RYTc5BkjEgSZUGJnjM5PISUB2tisjlsShcq87F4DuWWIOBnxjp1fkBTRC5xeJ4qz1I0ylh5-bz0JlrvrJ9ReduBcknBXn03oCrRV94890PIuZMQg80wQv8Fog73gAKCCWFMnqvNhIblZW9-pgUGaU6oxSn3QZp9LiOJ7OAudcxMA'}, {'domain': '.work.weixin.qq.com', 'expiry': 1636016498, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1604474850,1604480499'}, {'domain': '.qq.com', 'expiry': 1903410463, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_393769136'}, {'domain': '.qq.com', 'httpOnly': False, 'name': '_qpsvr_localtk', 'path': '/', 'secure': False, 'value': '0.915383500290541'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s5005294590'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1913860541, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147483646, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': '369c175d38b749fb00e2861045db6cfe386ddc31b3f49fa4a032bf2969e61802'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '393769136'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_si', 'path': '/', 'secure': False, 'value': 's1231096832'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324945173189'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '4309097464'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '5215330304'}, {'domain': '.qq.com', 'expiry': 2147483645, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': '9BRxmTLsYL'}]
        #     # 将cookie传值给浏览器,同时如果有expiry将其删除,删除key为expiry的这对键值对
        #     #
        #     # for cookie in cookies:
        #     #     if "expiry" in cookie.keys():
        #     #         cookie.pop("expiry")
        #     #     self.driver.add_cookie(cookie)

            # time.sleep(3)
            # self.driver.refresh()

        with allure.step("使用chrome debug模式，复用浏览器，跳过登录"):
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

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

            while  acctid <= 50:
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

