
"""
把框架中公共的方法抽离出来，方便调用
"""
import time

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

class BasePage:

    # basepage初始化了一个driver
    def __init__(self, driver:webdriver=None):
            self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_by_scroll(self, text):
        return self.find(MobileBy.ANDROID_UIAUTOMATOR,
                  'new UiScrollable(new UiSelector()'
                  '.scrollable(true).instance(0))'
                  '.scrollIntoView(new UiSelector()'
                  f'.text("{text}").instance(0));').click()

    def get_toast_text(self):
        toast_text = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return toast_text

    def step_main(self):
        by = None
        locator = None

        with open("../page/main.yml", encoding="utf-8") as f:
            steps = yaml.safe_load(f)
            # print(steps)

        for step in steps:
            # print(step)
            if "by" in step.keys():
                if step["by"] == "XPATH":
                    by = MobileBy.XPATH
                elif step["by"] == "ID":
                    by = MobileBy.ID
                elif step["by"] == "ACCESSIBILITY_ID":
                    by = MobileBy.ACCESSIBILITY_ID
            if "locator" in step.keys():
                locator = step["locator"]
            element = self.find(by, locator)
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()

    def step_contact_list(self, value = None):
        by = None
        locator = None

        with open("../page/contact_list.yml", encoding="utf-8") as f:
            steps = yaml.safe_load(f)
            # print(steps)

        for step in steps:
            # print(step)
            if "by" in step.keys():
                if step["by"] == "XPATH":
                    by = MobileBy.XPATH
                elif step["by"] == "ID":
                    by = MobileBy.ID
                elif step["by"] == "ACCESSIBILITY_ID":
                    by = MobileBy.ACCESSIBILITY_ID
            if "locator" in step.keys():
                locator = step["locator"]
            element = self.find(by, locator)
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()
                elif action == "send":
                    with open("../page/contact_list_value.yml", encoding = "utf-8") as file_value:
                        values = yaml.safe_load(file_value)
                        # print(values)
                    for value in values:
                        element.send_keys(value)
                        time.sleep(2)

