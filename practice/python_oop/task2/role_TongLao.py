# -*- coding:utf-8 -*-
# @time    :2020/10/25 17:14
# @Author  :dmingzhu
# @dmingzhu:role_TongLao.py

import random
"""
定义Tonglao类
属性：血量，武力值（通过参数得到）
方法：see_people,fight_zms
"""
class TongLao:
    """定义构造函数"""
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    """
    定义see_people函数
    1.判断见到的人
    2.打印对话
    """
    def see_people(self, name):
        if name == "WYZ":
            print("师弟！！")
        elif name == "李秋水":
            print("师弟是我的")
        elif name == "丁春秋":
            print("叛徒，我杀了你！！")
    """
    定义fight_zms函数
    1.计算打出折梅手后双方的武力值和血量
    2.根据血量判断输赢
    """
    def fight_zms(self, enemy_hp, enemy_power):
        self.hp = self.hp/2 - enemy_power
        self.power = self.power * 10
        enemy_hp = enemy_hp - self.power

        if self.hp > enemy_hp :
            print("我赢了")
        else:
            print("我输了")

if __name__ == "__main__":
    hp = 100
    power = 200
    enemy_hp = 300
    enemy_power = 300
    tonglao = TongLao(hp, power)

    name_list = ["WYZ", "李秋水", "丁春秋"]
    name = random.choice(name_list)
    tonglao.see_people(name)
    tonglao.fight_zms(enemy_hp, enemy_power)


