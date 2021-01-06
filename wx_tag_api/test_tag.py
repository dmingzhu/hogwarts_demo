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
        pass
    def test_get_corp_tag_list(self, tag_id):
        pass


    def test_add_crop_tag(self, group_name, tag_names):
        pass
    #   使用的哪几个参数的测试数据，在断言时，需要用对应的实际结果去判断是否输出正确，所以此处需要针对group_name 和tag_name都做断言

    def test_edit_corp_tag(self):
        pass

    def test_del_corp_tag(self):
        pass

