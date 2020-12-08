# -*- coding:utf-8 -*-
# @time    :2020/12/7 20:34
# @Author  :dmingzhu
# @dmingzhu:test_tag.py
import json

import pytest
from jsonpath import jsonpath

from wx_tag_api.tag import Tag


class TestTag:
    # todo:清理测试环境
    def setup(self):
        self.tag = Tag()
        # 调用get_token()给self.token赋值
        self.tag.get_token()

    #todo:获取所有
    @pytest.mark.parametrize("tag_ids",[
        ([])
    ])
    def test_get_corp_tag_list(self, tag_ids):
        r = self.tag.get_corp_tag_list(tag_ids=tag_ids)
        print(json.dumps(r, indent=2))

    @pytest.mark.parametrize("group_name, tag_names", [
        # 新建标签组，添加1个标签
        ("111", [{"name":"aaa"}]),
        # 新建标签组，添加2个标签
        ("222", [{"name": "bbb"}, {"name":"ccc"}])
        # 新建标签组，不添加标签

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

    # @pytest.mark.parametrize("tag_ids, group_ids",[
    #     #指定标签组
    #     ([], )
    # ])
    # def test_del_corp_tag(self, tag_ids):
    def test_del_corp_tag(self):
        #先查列表
        tag_ids = []
        r_list = self.tag.get_corp_tag_list(tag_ids=tag_ids)
        tag_group = r_list["tag_group"]
        print("打印tag_group",json.dumps(tag_group, indent=2))
        tag_list = []
        for tag in tag_group["tag"]:
            print("打印tag", tag)
            if "id" in tag:
                tag_list.append(tag["id"])
        print("打印tag_list",tag_list)
        print(json.dumps(r_list,  indent=2))
        r = self.tag.del_corp_tag(tag_ids=tag_list)
        print("删除",r)

