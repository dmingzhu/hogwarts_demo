# -*- coding:utf-8 -*-
# @time    :2020/12/7 20:34
# @Author  :dmingzhu
# @dmingzhu:tag.py
import json

import requests


class Tag:
    """获取token"""
    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        param={
            "corpid":"ww69694e10de384523",
            "corpsecret":"_yb7L6V2q0Guqk44vdR9ju7fAjDYH8IH6_9nwp7472c"
        }
        r = requests.get(url=url, params=param)
        # print(json.dumps(r.json(), indent = 2))
        return r.json()["access_token"]

    """获取列表"""
    def get_corp_tag_list(self, tag_id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list"
        param = {
            "access_token":self.get_token()
        }
        json = {
            "tag_id": tag_id
        }
        r = requests.post(url=url, params=param, json=json)
        # print(json.dumps(r.json(), indent=2))
        return r.json()

    """添加标签"""
    def add_crop_tag(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag"
        param = {
             "access_token": self.get_token()
         }
        data = {
        "group_name": "GROUP_NAME_1207",
        "order": 1,
        "tag": [{
            "name": "TAG_NAME_1",
            "order": 1
        }
    ]
}
        r = requests.post(url=url , params=param,  json= data)
        # print(json.dumps(r.json(), indent=2))
        return r.json()

    def edit_corp_tag(self):
        pass

    def del_corp_tag(self):
        pass


if __name__ == "__main__":
    AA = Tag()
    # AA.get_token()
    # AA.get_corp_tag_list()
    AA.add_crop_tag()