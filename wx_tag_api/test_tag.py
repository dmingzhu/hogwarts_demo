# -*- coding:utf-8 -*-
# @time    :2020/12/7 20:34
# @Author  :dmingzhu
# @dmingzhu:test_tag.py
import json

import pytest
from jsonpath import jsonpath

from wx_tag_api.tag import Tag


class TestTag:
    def setup(self):
        self.tag = Tag()
        # 调用get_token()给self.token赋值
        self.tag.get_token()

    #todo:测试获取企业标签库
    def test_get_corp_tag_list(self, tag_id):
        self.tag.get_corp_tag_list(tag_id=tag_id)

    @pytest.mark.parametrize("group_name, tag_names", [
        # 标签组名，单个标签名
        ("111", [{"name":"333"}]),
        #标签组名，多个标签名
        ("111", [{"name": "tag_name1"},{"name":"tag_name2"}])
        #标签组名，不存在的标签名
    #     没有
    ])
    def test_add_crop_tag(self, group_name, tag_names):
        r = self.tag.add_crop_tag(group_name=group_name, tag_names=tag_names)
        print(json.dumps(r, indent=2))
        # 获取taget_id，存在列表里
        tag_id = jsonpath(r, "$..tag_group.tag[0].id")
        r_list = self.tag.get_corp_tag_list(tag_id)
        print(json.dumps(r_list, indent=2))
        # 判断get_list返回值中存在添加的tag name
        group = [group for group in r_list["tag_group"] if group["group_name"] == group_name][0]
        tags = [{"name":tag["name"]} for tag in group["tag"]]
        print(group)
        print(tags)
    #   使用的哪几个参数的测试数据，在断言时，需要用对应的实际结果去判断是否输出正确，所以此处需要针对group_name 和tag_name都做断言

    def test_edit_corp_tag(self):
        pass

    def test_del_corp_tag(self):
        pass

