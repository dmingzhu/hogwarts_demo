import requests


class Tag:
    """根据corpid， corpsecret获取token"""
    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param = {
            "corpid":"ww69694e10de384523",
            "corpsecret":"pFx93CTsV-VwCe9Or5SscVi-Zt2M_ooIyRUpjRMPIJ8"
        }
        r = requests.get(url=url,  params=param)
        print("打印token", r.json()["access_token"])
        return r.json()["access_token"]

if __name__ == "__main__":
    aa = Tag()
    aa.get_token()