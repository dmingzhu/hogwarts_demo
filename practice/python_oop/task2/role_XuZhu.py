# -*- coding:utf-8 -*-
# @time    :2020/10/25 17:36
# @Author  :dmingzhu
# @dmingzhu:role_XuZhu.py

from practice.python_oop.task2 import role_TongLao

"""
定义XuZhu类
1.read方法
"""
class XuZhu(role_TongLao.TongLao):
    """
    定义read方法
    1.直接打印“罪过，罪过”
    """
    def read(self):
        print("罪过罪过")


if __name__ == "__main__":
    hp = 100
    power = 200
    xuzhu = XuZhu(hp, power)
    xuzhu.read()