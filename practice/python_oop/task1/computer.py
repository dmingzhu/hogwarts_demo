# -*- coding:utf-8 -*-
# @time    :2020/10/25 17:12
# @Author  :dmingzhu
# @dmingzhu:Phone.py

"""
定义一个computer类
"""
class Computer:
    def __init__(self, brand, cpu,memory):
        self.brand = brand
        self.cpu = cpu
        self.memory = memory

    def work(self):
        print("用于平时工作")

    def paint(self):
        print("可以画图")

    def entertainment(self):
        print("可以娱乐")

my_computer = Computer("hp", "intel i5", "16G")
print(my_computer.memory)
my_computer.work()
my_computer.paint()
my_computer.entertainment()

