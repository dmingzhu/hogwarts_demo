from selenium import webdriver
from selenium.webdriver.common.by import By


class base:
    def setup(self):
        opt = webdriver.ChromeOptions()
        # opt.add_argument("--disable-gpu")
        opt.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(3)
        return self.driver

    def teardown(self):
        self.driver.quit()

    # 封装find_element
    def find(self, by, locator):
        # 调用类方法，获取到self.driver
        self.setup()
        return self.driver.find_element(by, locator)


if __name__ == "__main__":
    locator = '//*[@class="ww_indexImg ww_indexImg_AddMember"]'
    by = By.XPATH
    base().find(by, locator)

