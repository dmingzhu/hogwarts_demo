import json

import requests
#todo:改造成api object
#todo:使用jsonpath
#todo:使用hamcrest做断言
from wework_api_framework.wework import WeworkApi


class TagApi(WeworkApi):

    """创建标签"""
    def creat_tag(self, creat_data):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/create"
        r_add = requests.post(url=url, params = {"access_token":self.token}, json = creat_data)
        print("创建标签", r_add.json())

    """获取tag列表"""
    def get_tag_list(self):
        """获取标签列表"""
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/list'
        token_json = {"access_token":self.token}
        r_list = requests.get(url=url, params=token_json)
        print("获取标签列表",r_list.json())

    def del_tag_list(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/delete"
        param = {
            "access_token": self.token,
            "tagid" : 12
        }
        r = requests.get(url=url, params=param)
        print("删除标签", r.json())

    def add_tag_member(self):
        """增加标签成员"""
        url2 = 'https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers'
        token_data = {"access_token":self.token}
        member_data = {
            # 需要先创建一个标签，再在这个标签下去添加成员
            "tagid": 13,
            # 成员唯一标识：账号，一定要是在通讯录中已经存在的,也就是说，增加标签成员，传的是成员ID
            "userlist": ["user_tag_01", "user_tag_02"]
        }
        r_tag_member = requests.post(url=url2, params=token_data,json=member_data)
        print("增加标签成员",r_tag_member.json())


    def get_tag_member_list(self):
        """获取成员列表"""
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/get'
        param = {"access_token":self.token, "tagid":13}
        r_tag_memlist = requests.get(url=url, params=param)
        print("获取标签成员",r_tag_memlist.json())

    def del_tag_member_list(self):
        pass

if __name__ == "__main__":
    # TagApi().del_tag_list()
    TagApi().get_tag_list()
    TagApi().get_tag_member_list()


