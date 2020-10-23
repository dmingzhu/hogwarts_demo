# -*- coding:utf-8 -*-
# @time    :2020/10/23 16:22
# @Author  :dmingzhu
# @dmingzhu:game_round_more.py

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""

def fight():
    # 初始化“我”的血量值
    my_hp = 1000
    # 初始化“我”的攻击值
    my_power = 200

    # 初始化“敌人”的血量值
    enemy_hp = 1000
    # 初始化“敌人”的攻击值
    enemy_power = 100

    # 循环执行游戏
    while True:
        my_hp = my_hp - enemy_power
        enemy_hp = enemy_hp - my_power

        print(my_hp)
        # 对每轮循环后的结果进行判断
        if my_hp < 0:
            print("我输了")
            # 一旦if条件达到，break跳出全部循环
            break
        elif enemy_hp < 0:
            print("我赢了")
            break


fight()