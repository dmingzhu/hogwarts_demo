import json

import pytest
import requests

from wx_tag_api.tag import Tag

class TestTag():
    def setup(self):
        self.tag = Tag().get_token()

    @pytest.mark.parametrize("group_name, tag_name_list",[
        #添加多个标签
        ("group_add_success1", [{"name": "tag_1"}, {"name": "tag_2"}]),
        #添加单个标签
        ("group_add_success2", [{"name": "tag_2"}])]
        )
    def test_tag_add(self, group_name, tag_name_list):
        """
        测试添加成功的场景
        规则：
        1.在指定的标签组下添加标签，group_id必填，如果填了group_id，则group_name和标签组的order参数会被忽略
        2.在新标签组下添加标签，group_name必填，group_name如果存在，则在其下添加标签
        3.标签组内的标签不能重名，传入多个标签只会创建一个
        :return:
        """
        add  = self.tag[1].add(group_name=group_name, tag_name_list=tag_name_list)
        add_json = json.dumps(add.json(), indent=2)
        # print(add_json)
        # print(json.loads(add_json)["errcode"])
        tag_list = self.tag[1].list()
        tag_list_json = json.dumps(tag_list.json(), indent=2)
        # print(type(tag_list_json))
        # print(tag_list_json)
        print(json.loads(tag_list_json)["tag_group"][0]["group_name"])
        # print(json.loads(tag_list_json)["group_name"])
        assert json.loads(add_json)["errcode"] == 0
        # assert json.loads(tag_list_json)["tag_group"][0]["group_name"] == group_name


    @pytest.mark.parametrize(
        "group_name,tag_name_list",[
            #添加空标签
            ("group_add_fail1",[]),
            #不支持创建空标签组
            ("",[{"name":"tag_fail1"}])
        ]
    )
    def test_tag_add_fail(self, group_name, tag_name_list):
        """
        添加失败的用例
        :return:
        """
        add  = self.tag[1].add(group_name=group_name, tag_name_list=tag_name_list)
        add_json = json.dumps(add.json(), indent=2)
        if tag_name_list == []:
            assert json.loads(add_json)["errcode"] == 41018
        elif group_name == "":
            assert json.loads(add_json)["errcode"] == 40063

    def test_tag_delete(self):
        """
        测试删除
        :return:
        """
        tag_list = self.tag[1].list()
        tag_list_json = json.dumps(tag_list.json(), indent=2)
        group_ids = []
        group_id = json.loads(tag_list_json)["tag_group"][0]["group_id"]
        group_ids.append(group_id)
        # print(group_ids)
        delete_tag = self.tag[1].delete(tag_ids=None, group_ids=group_ids)
        # print(delete_tag.json())
        tag_list_delete = self.tag[1].list()
        print(tag_list_delete.json())
        assert tag_list_delete.json()["errcode"] == 0
        assert tag_list_delete.json()["tag_group"] == []
        #判断group_id不在现在的列表中

    def test_clear_all(self):
        r = self.tag[1].clear_all()
        print(r.json())
        assert r.json()["errcode"] == 0
        assert r.json()["tag_group"] == []

    def test_edit(self):
        old_group = "group_add_success2"
        new_group = "group_edit_01"
        r = self.tag[1].edit(old_group_name=old_group, new_group_name=new_group)
        tag_group = r[0].json()["tag_group"]
        for i in tag_group:
            if i["group_id"] == r[1]:
                assert i["group_name"] == new_group


