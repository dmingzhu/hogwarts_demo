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
    """
    获取标签列表
    获取标签列表doc url：https://work.weixin.qq.com/api/doc/90000/90135/90216
    """
    url1 = 'https://qyapi.weixin.qq.com/cgi-bin/tag/list'
    token_data = {"access_token":token}
    r_list = requests.get(url=url1, params=token_data)
    print(r_list.json())
    assert r_list.status_code == 200
    assert r_list.json()["errmsg"] == "ok"

    """
    添加标签列表成员 
    """
    url2 = "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers"
    add_data = {
        "tagid": 12,
        "userlist":[ "user1","user2"],
        "partylist": [4]
        }
    r_add = requests.post(url=url2, params=add_data, json=token_data)
    print(r_add.json())
    assert r_add.status_code == 200
