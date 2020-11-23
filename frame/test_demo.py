import pytest
import yaml
from appium.webdriver import WebElement
from selenium import webdriver


def load_data(path="D:/hogwarts_demo/frame/test_data.yaml"):
    # path = "./test_data.yaml"
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


class TestSearch:

    # def setup(self):
    #     opt = webdriver.ChromeOptions
    #     opt.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=opt)

    # todo: 加入异常操作：如弹窗处理
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # 要注意，yaml文件的后缀名是yaml
    @pytest.mark.parametrize("data", load_data()["data"])
    def test_search(self, data):
        steps = load_data()["steps"]
        for step in steps:
            element:WebElement = None
            #解析webdriver, 是chrome则用chrome驱动
            if "webdriver" in step:
                browser = step["webdriver"]["browser"]
                if browser == "chrome":
                    self.driver = webdriver.Chrome()

                if browser == "firefox":
                    self.driver = webdriver.Firefox()

            if "get" in step:
                url = step["get"]
                # print(url)
                self.driver.get(url)
                self.driver.implicitly_wait(3)

            if "find_element" in step:
                locator_data = step["find_element"]
                print(list(locator_data.keys()))
                if "by" in locator_data.keys():
                    element = self.find(locator_data["by"], locator_data["locator"])
                if "click" in locator_data.keys():
                    element.click()
                if "send_keys" in locator_data.keys():
                    send_values:str = str(locator_data["send_keys"])
                    send_values = send_values.replace("{data}", data)
                    element.send_keys(send_values)

