import json

import pytest
from jsonpath import jsonpath

from wework_api_framework.tag import TagApi
from wework_api_framework.wework import WeworkApi
import hamcrest
from jsonschema import validate


class TestTag:
    def setup(self):
        self.api = TagApi()

    @pytest.mark.parametrize("tag_name, tag_id", [
        (f"tag_UI_13", 13)
    ])
    @pytest.mark.run(order=1)
    def test_creat_tag(self, tag_name, tag_id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/create"
        creat_data = {
            "tagname": tag_name,
            "tagid": tag_id
        }
        r = self.api.creat_tag(url, creat_data)
        r_tag = jsonpath(r, "$..tagid")

        # print(r_tag[0])
       #断言tag_id
        hamcrest.assert_that(int(r_tag[0]), hamcrest.equal_to(int(tag_id)))
    # {'errcode': 0, 'errmsg': 'created', 'tagid': 15}
    # {'errcode': 40068,
     # 'errmsg': 'invalid tagid, hint: [1606914098_53_9fa918a40d0343b59fd6f03bdd1eccee], from ip: 171.113.235.79, more info at https://open.work.weixin.qq.com/devtool/query?e=40068'}

    @pytest.mark.run(order=2)
    def test_get_tag_list(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/list'
        r = self.api.get_tag_list(url)
        r_msg = jsonpath(r, "$..errmsg")
        hamcrest.assert_that(r_msg[0], hamcrest.equal_to("ok"))



    @pytest.mark.parametrize("tag_id, user_list", [
        # (13, ["user_tag_01", "user_tag_02"]),
        (13, ["user_tag_03"])
    ])
    def test_add_tag_user(self, tag_id, user_list):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers'
        r = self.api.add_tag_user(url, tag_id, user_list)
        assert r["errmsg"] == "ok"

    def test_get_tag_user(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/get'
        tag_id = 13
        r = self.api.get_tag_user_list(url=url, tag_id=tag_id)
        assert r["errmsg"] == "ok"
        return r

    def test_del_tag_user(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers'
        tag_id = 13
        r_user_list = self.test_get_tag_user()["userlist"]
        # print(r_user_list)
        user_list = []
        for user in r_user_list:
            for k in user:
                if k == "userid":
                    user_list.append(user[k])
        # print(user_list)
        r = self.api.del_tag_user(url=url, tag_id=tag_id, user_list=user_list)
        print(r)
        assert r["errmsg"] == "ok"

    @pytest.mark.parametrize("tagid", [(13)])
    @pytest.mark.run(order=3)
    def test_del_tag(self, tagid):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/delete"
        r = self.api.del_tag(url, tagid)
        # print(r)
        assert r["errmsg"] == "deleted"

