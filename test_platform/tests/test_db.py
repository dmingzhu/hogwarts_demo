# -*- coding:utf-8 -*-
# @time    :2021/1/6 23:33
# @Author  :dmingzhu
# @dmingzhu:test_db.py
from test_platform.src.backend import db, TestCase


def test_create_table():
    # 用于生成表
    db.create_all()
    # case2 = TestCase(name = "case2", description = "description2", steps = ["1.查看,2.提交"])
    # db.session.add(case2)
    # db.session.commit()

