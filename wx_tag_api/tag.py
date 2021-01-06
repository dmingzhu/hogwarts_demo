# -*- coding:utf-8 -*-
# @time    :2020/12/7 20:34
# @Author  :dmingzhu
# @dmingzhu:tag.py
import json

import requests
corpid = "ww69694e10de384523"
corpsecret = "_yb7L6V2q0Guqk44vdR9ju7fAjDYH8IH6_9nwp7472c"

class Tag:
    """
    构造一个类变量存token
    """
    def __init__(self):
        self.token = ""

    """
    封装获取token
    """
    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param={
            "corpid":corpid,
            "corpsecret":corpsecret
        }
        r = requests.get(url=url, params=param)
        # print(json.dumps(r.json(), indent = 2))
        self.token =  r.json()["access_token"]

    """
    获取列表
    """
    def get_corp_tag_list(self, tag_ids):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        param = {
            "access_token":self.token
        }
        json = {
            "tag_id": tag_ids
        }
        r = requests.post(url=url, params=param, json=json)
        # print(json.dumps(r.json(), indent=2))
        return r.json()

    """
    添加标签
    """
    def add_crop_tag(self, group_name, tag_names):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        param = {
             "access_token": self.token
         }
        json = {
            "group_name": group_name,
            "tag": tag_names
            }

        r = requests.post(url=url , params=param,  json= json)
        # print(json.dumps(r.json(), indent=2))
        return r.json()

    def edit_corp_tag(self):
        pass

    def del_corp_tag(self, tag_ids):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag"
        param = {
            "access_token": self.token
        }
        json = {
            # tag_ids，group_id列表
            "tag_id":tag_ids
        }
        r = requests.post(url=url, params=param, json=json)
        return r.json()

if __name__ == "__main__":
    AA = Tag()
    AA.get_token()
    # AA.get_corp_tag_list()
    # AA.add_crop_tag()