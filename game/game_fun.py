# -*- coding:utf-8 -*-
# @time    :2020/10/23 16:44
# @Author  :dmingzhu
# @dmingzhu:game_fun.py

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""

# 让“敌人”的血量和攻击值随机产生
import random


def fight(enemy_hp, enemy_power):
    # 初始化“我”的血量值
    my_hp = 1000
    # 初始化“我”的攻击值
    my_power = 200

    # 打印“敌人”的血量和攻击值
    print(f"敌人的血量是：{enemy_hp},攻击值是：{enemy_power}  \n ")

    # 初始化游戏轮次
    num = 1

    # 循环执行游戏
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power
        # 打印双方的剩余血量
        print(f"第{num}轮,我的剩余血量是{my_hp},敌人的剩余血量是{enemy_hp}")
        # 对每轮循环后的结果进行判断
        if my_hp < 0:
            print("我输了")
            # 一旦if条件达到，break跳出全部循环
            break
        elif enemy_hp < 0:
            print("我赢了")
            break
        else:
            # 游戏未终止则轮次—+1，开始下一轮
            num = num + 1


#如果当前py文件的name是main则执行下面的代码块
if __name__ == '__main__':

    hp = [x for x in range(990, 1010)]
    # 从hp列表中随机选择一个值赋给enemy_hp
    enemy_hp = random.choice(hp)

    # 将随机生成的一个整型随机数赋enemy_power
    enemy_power = random.randint(300, 600)
    # 调用函数并传参
    fight(enemy_hp, enemy_power)

