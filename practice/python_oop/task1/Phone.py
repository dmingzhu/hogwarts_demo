# -*- coding:utf-8 -*-
# @time    :2020/10/25 17:12
# @Author  :dmingzhu
# @dmingzhu:Phone.py

"""
定义一个phone类
"""
class Phone:
    def __init__(self, brand, level,memory):
        self.brand = brand
        self.level = level
        self.memory = memory

    def games(self):
        print("手机安装app，可以打游戏")

    def call(self):
        print("可以和别人通话，交流")

    def take_photos(self):
        print("可以照相")

    def note(self):
        print("可以工作，做笔记备忘")

my_phone = Phone("apple", 7, 128)
print(my_phone.memory)
my_phone.games()
my_phone.call()
my_phone.take_photos()
my_phone.note()

