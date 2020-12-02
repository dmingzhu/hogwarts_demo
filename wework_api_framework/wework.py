#封装wework公用的api
import requests


class WeworkApi:
    def __init__(self):
        self.token = ""

    def get_token(self):
        url_get_token= ' https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        param = {
            "corpid": "ww69694e10de384523",
            "corpsecret": "pFx93CTsV-VwCe9Or5SsceN_4MGAAaCHbcISj7CpQWQ"
        }
        r = requests.get(url=url_get_token, params=param)
        self.token = r.json()["access_token"]
        # return TagApi(self.token)