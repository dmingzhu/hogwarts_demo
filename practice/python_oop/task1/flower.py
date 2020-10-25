# -*- coding:utf-8 -*-
# @time    :2020/10/25 13:31
# @Author  :dmingzhu
# @dmingzhu:flower.py
import random
import time
import math
import datetime

"""
定义花类
初始化构造实例变量：名称, 香味, 每天的浇水量, 天数, 共计浇水量
计算规则：
    1.共计浇水量：total_water = days * watering
    2.共计光照：根据每天随机生成的光照值求和, 随机的范围是从1到150
    3.截止当前目标光照值：self.target_light = self.days * 150 
    4.需要的肥料颗数：1500-当前已有的光照值，结果向上取整
场景：
    默认随机生长10天，对10天后的光照值进行判断：
    1.光照值大于等于目标光照值：生长状况好，开出2朵花，香味淡
    2.光照值介于目标光照值和目标光照值-500：生长状况一般，开出1朵花，香味无，并计算出需要肥料颗数
    3.光照值小于目标光照值-500：生长不佳，没有开花，并计算出需要肥料颗数
"""



class flower:

    def __init__(self, name, watering, days):
        self.name = name
        self.perfume = ["no", "fresh", "strong"]
        self.watering = watering
        self.days = days
        self.total_water = self.watering * self.days

    """
    定义count_water函数
    直接返回当前的总浇水量
    """
    def count_water(self):
        # print(f"每天浇水{self.watering}L, {self.days}天后,目前总浇水量是{self.total_water}")
        return self.total_water

    """
    定义count_light函数
    计算当前的总光照值
    """
    def count_light(self):
        self.total_light = 0
        for day in range(1, self.days+1):
            self.light_num = random.randint(50, 150)
            self.total_light = self.light_num +self.total_light
            # print(f"第{day}天，光照值是{self.light_num},累计光照值是{self.total_light}")
        return self.total_light

    """
    定义count_element函数
    计算当前所需的肥料颗数
    """
    def count_element(self):
        if self.count_light() < 1500 :
            element_num = math.ceil(1500 - self.count_light())
            return element_num
    """
    定义use_element函数
    打印出使用肥料20天后的生长状态
    返回20天后的总光照值
    """
    def use_element(self):
        self.days = self.days + 20
        self.total_light = self.days * 150
        print(f"又过20天之后，开出5朵花，香味：{self.perfume[2]}")
        return self.total_light

    """
    记录生长日志，
    根据当前光照值，判断当前花的生长情况
    需要给肥料则调用，use_elemennt(),不需要给肥料，则直接打印20天后的结果
    """
    def grow_diary(self):
        print(f"《{self.name}生长日记》")
        start_time = datetime.date.today()
        print(f"{start_time},买回来一株小花苗,开始记录生长情况")
        time.sleep(1)
        end_time = start_time + datetime.timedelta(days = self.days)
        print(f"{end_time},{self.days}天后，共计浇水量{self.total_water},光照{self.total_light}")

        light_num = self.count_light()
        self.target_light = self.days * 150
        if light_num >= self.target_light:
            print(f"生长状况好，开出2朵花，香味：{self.perfume[1]}")

        elif light_num < self.target_light and light_num >= (self.target_light - 500) :
            print(f"生长状况一般，开出1朵花，香味：{self.perfume[0]}, 需要给{self.count_element()}颗肥料！")
            is_use_element = input("确定是否给肥料，y/n?")
            if is_use_element == "y":
               self.use_element()
            else:
                print("又20天，植物没怎么长")

        elif light_num < (self.target_light - 500):
            print(f"生长不佳，没有开花，需要给{self.count_element()}颗肥料！")
            is_use_element = input("确定是否给肥料，y/n?")
            if is_use_element == "y":
                self.use_element()
            else:
                print("又过20天，植物死了")



name = "sunflower"
watering = 1
days = 10
sunflower = flower(name, watering, days)
sunflower.count_light()
sunflower.count_water()
sunflower.grow_diary()

