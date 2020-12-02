import json

import requests


def test_tag():
    # 获取token

    """
    获取token
    """

    url_get_token= ' https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    param = {
        "corpid" : "ww69694e10de384523",
        "corpsecret" : "pFx93CTsV-VwCe9Or5SsceN_4MGAAaCHbcISj7CpQWQ"
    }
    r = requests.get(url=url_get_token, params=param)
    token = r.json()["access_token"]
    print(token)
    print(r.json())
    assert r.json()["errmsg"] == "ok"

    """创建标签"""
    url2 = "https://qyapi.weixin.qq.com/cgi-bin/tag/create"
    r_add = requests.post(
        url=url2,
        params = {"access_token":token},
        json={
            "tagname": "tag_UI_13",
            "tagid": 13
    }
    )
    # print("创建标签",r_add.json())
    # # assert r_add.status_code == 200

    """
    获取标签列表
    获取标签列表doc url：https://work.weixin.qq.com/api/doc/90000/90135/90216
    """
    url1 = 'https://qyapi.weixin.qq.com/cgi-bin/tag/list'
    token_data = {"access_token":token}
    r_list = requests.get(url=url1, params=token_data)
    print("获取标签列表",r_list.json())
    assert r_list.status_code == 200
    assert r_list.json()["errmsg"] == "ok"

    """增加标签成员"""
    url2 = 'https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers'
    token_data = {"access_token":token}
    member_data = {
        # 需要先创建一个标签，再在这个标签下去添加成员
        "tagid": 13,
        # 成员唯一标识：账号，一定要是在通讯录中已经存在的,也就是说，增加标签成员，传的是成员ID
        "userlist": ["user_tag_01", "user_tag_02"]
    }
    r_tag_member = requests.post(url=url2, params=token_data,json=member_data)
    print("增加标签成员",r_tag_member.json())
    assert r_tag_member.status_code == 200
    assert r_tag_member.json()["errmsg"] == "ok"


    """获取成员列表"""
    url1 = 'https://qyapi.weixin.qq.com/cgi-bin/tag/get'
    param = {"access_token":token, "tagid":13}
    r_tag_memlist = requests.get(url=url1, params=param)
    print("获取标签成员",r_tag_memlist.json())
    assert r_tag_memlist.status_code == 200
    assert r_tag_memlist.json()["errmsg"] == "ok"