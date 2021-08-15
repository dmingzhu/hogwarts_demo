# -*- coding:utf-8 -*-
# @time    :2021/7/17 13:15
# @Author  :dmingzhu
# @dmingzhu:test_bb.py
from datetime import datetime

import requests


def test_case_get():
    url= "http://127.0.0.1:5000/testcase"

    r = requests.post(url=url,
                      json = {
                          "name":f"name01 {datetime.now().isoformat()}",
                          "description":"opretion",
                          "steps":["1.", "2.", "3."]
                      }
                      )

    r_get = requests.get(url=url)

    # print(r_get.json())
    assert r.status_code == 200
    assert r_get.status_code == 200

def test_case_delete():
    url = "http://127.0.0.1:5000/testcase"
    # 用params方式传递参数，服务端要用request.args.get()获取
    # rr = requests.get(url, args={"id":2})
    # 用json方式传参，服务端需用request.json.get()获取
    # rr = requests.get(url, json={"id":5})
    r = requests.delete(url, json={"id":3})
    # print(rr.json())
    # assert rr.status_code == 200
    assert r.status_code == 200

def test_task_post():
    url = "http://127.0.0.1:5000/testtask"
    r = requests.post(url=url,
                      json={
                          "case_id":"3",
                          "name":"task_name_1",
                          "description":"task_description_1"
                      })
    assert r.status_code == 200

def test_task_get():
    url = "http://127.0.0.1:5000/testtask"
    r = requests.get(url)
    print(r)


def test_task_run():
    url = "http://127.0.0.1:5000/testtask"
    r = requests.put(url=url,
                      json={
                          "id":1
                      })
    print(r.json())
    assert r.status_code == 200

