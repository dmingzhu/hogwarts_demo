# -*- coding:utf-8 -*-
# @time    :2021/1/6 23:37
# @Author  :dmingzhu
# @dmingzhu:test_backend.py

import requests

# 测试testcase服务
from jenkinsapi.jenkins import Jenkins


def test_testcase_post():
    url = "http://127.0.0.1:8384/testcase"

    # 带json使用post方法访问资源
    r = requests.post(url,
                  json={
                      "name": "case6",
                      "description": "description6",
                      # "steps": ["1填写", "2提交", "3审批"]
                      "steps":"1, 2, 3"
                  })
    print(r.json())
    # assert r.status_code == 200
    r_get = requests.get(url)
    print(r_get.json())
    # assert r_get.json()



def test_task_post():
    url = "http://127.0.0.1:8384/task"
    r_post = requests.post(url,
                  json={
                      "name": "task_03",
                      "testcase_id": 3
                  })
    r_get = requests.get(url)
    # print(r_post.json())
    print(r_get.json())
    # assert r_get.json()


def test_task_run():
    url = "http://127.0.0.1:8384/task"
    r = requests.put(url,
                  json={
                      'id': 1
                  }
                     )

    print(r.json())
    assert r.status_code == 200
    assert r.json()["msg"] == "ok"
