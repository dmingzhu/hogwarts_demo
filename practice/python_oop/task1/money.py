# -*- coding:utf-8 -*-
# @time    :2020/10/25 18:29
# @Author  :dmingzhu
# @dmingzhu:money.py

"""
定义一个money类
"""
class Money:
    def __init__(self, face_value, amount):
        self.face_value = face_value
        self.cpu = amount

    def go_to_school(self):
        print("用于上学")

    def for_insurance(self):
        print("可以用作生活保障")

    def for_family(self):
        print("可以照顾家人")

my_money = Money("100", 1000)
my_money.for_insurance()
my_money.for_family()
