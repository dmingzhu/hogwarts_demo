# -*- coding:utf-8 -*-
# @time    :2020/10/23 15:48
# @Author  :dmingzhu
# @dmingzhu:game_round1.py

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""

# 初始化“我”的血量值
my_hp = 1000
# 初始化“我”的攻击值
my_power = 200

# 初始化“敌人”的血量值
enemy_hp = 1000
# 初始化“敌人”的攻击值
enemy_power = 200

"""
定义fight方法
作用：实现比较游戏双方的剩余血量值，返回“我”的游戏结果
"""
def fight():
    # 定义"我"剩余血量的计算规则
    my_final_hp = my_hp - enemy_power
    # 定义"敌人"剩余血量的计算规则
    enemy_final_hp = enemy_hp - my_power
    #比较两者剩余血量,“我”的血量大于“敌人”则我赢，否则“敌人”赢
    # if my_final_hp > enemy_final_hp:
    #     print("我赢了")
    # else:
    #     print("我输了")

    #用三目运算的形式写条件判断，适用范围：分支条件简单
    print("我赢了") if my_final_hp > enemy_final_hp else print("我输了")


#如果当前py文件的name是main则执行fight()
if __name__ == '__main__':
    fight()