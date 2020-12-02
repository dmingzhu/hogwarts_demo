import json

import requests
#todo:改造成api object
#todo:使用jsonpath
#todo:使用hamcrest做断言
from wework_api_framework.wework import WeworkApi


class TagApi(WeworkApi):
    """创建标签"""
    def creat_tag(self, url, creat_data):
        r = requests.post(url=url,
                              params = {"access_token":self.token},
                              json = creat_data)
        return r.json()

    """获取tag列表"""
    def get_tag_list(self, url):
        """获取标签列表"""
        token_json = {"access_token":self.token}
        r = requests.get(url=url, params=token_json)
        print("获取标签列表",r.json())
        return r.json()

    def del_tag(self, url, tagid):
        param = {
            "access_token" : self.token,
            "tagid" : tagid

        }
        r = requests.get(url=url, params=param)
        print("删除标签", r.json())
        return r.json()

    def add_tag_user(self, url, tag_id, user_list):
        """增加标签成员"""
        token_data = {"access_token":self.token}
        user_data = {
            # 需要先创建一个标签，再在这个标签下去添加成员
            "tagid": tag_id,
            # 成员唯一标识：账号，一定要是在通讯录中已经存在的,也就是说，增加标签成员，传的是成员ID
            # "userlist": ["user_tag_01", "user_tag_02"]
            "userlist":user_list
        }
        r = requests.post(url=url, params=token_data, json=user_data)
        print("增加标签成员",r.json())
        return r.json()

    def get_tag_user_list(self, url, tag_id):
        """获取成员列表"""
        param = {"access_token":self.token, "tagid":tag_id}
        r = requests.get(url=url, params=param)
        print("获取标签成员",r.json())
        return r.json()

    def del_tag_user(self, url, tag_id, user_list):
        """删除标签成员"""
        param = {"access_token":self.token}
        user_data={
            "tagid":tag_id,
            "userlist":user_list
        }
        r = requests.post(url=url, params=param, json=user_data)
        return r.json()

if __name__ == "__main__":
    aa = TagApi()
    user_list = [ "user_tag_01"]
    url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/get'

    aa.add_tag_user(url, tag_id=13, user_list=user_list)
    aa.get_tag_user_list()
