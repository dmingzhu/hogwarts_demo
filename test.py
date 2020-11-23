import pytest
import yaml
from selenium import webdriver


class TestSearch:
    # def setup(self):
    #     opt = webdriver.ChromeOptions
    #     opt.debugger_address = "127.0.0.1:9222"
    #     self.driver = webdriver.Chrome(options=opt)

    def find(self):
        pass

    def load_data(self, path):
        # path = "./test_data.yaml"
        with open(path, encoding = "utf-8") as f:
            return yaml.safe_load(f)

    # @pytest.mark.parametrize("data", load_data("./test_data.yaml")["data"])
    # def test_search(self):
    #     pass




if __name__ == "__main__":
    aa = TestSearch()
    # print(aa.load_data(path="D:/hogwarts_demo/frame/test_data.yaml")["data"])
    steps = aa.load_data(path="D:/hogwarts_demo/frame/test_data.yaml")["steps"]
    i = 0
    for step in steps :
        i += 1
        print(i, step)