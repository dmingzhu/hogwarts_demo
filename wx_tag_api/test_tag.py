# -*- coding:utf-8 -*-
# @time    :2020/12/7 20:34
# @Author  :dmingzhu
# @dmingzhu:test_tag.py
import json

from jsonpath import jsonpath

from wx_tag_api.tag import Tag


class TestTag:
    def setup(self):
        self.tag = Tag()

    def test_get_corp_tag_list(self):
        self.tag.get_corp_tag_list()

    def test_add_crop_tag(self):
        r = self.tag.add_crop_tag()
        # print(json.dumps(r, indent=2))
        # 获取tagget_id
        tag_id = jsonpath(r, "$..tag_group.tag[0].id")[0]
        r_list = self.tag.get_corp_tag_list(tag_id)
        # print(json.dumps(r_list, indent=2))
        assert r_list["tag_group"][0]["tag"][0]["name"] == "TAG_NAME_1"

    def test_edit_corp_tag(self):
        pass

    def test_del_corp_tag(self):
        pass

