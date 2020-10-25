# -*- coding:utf-8 -*-
# @time    :2020/10/25 11:03
# @Author  :dmingzhu
# @dmingzhu:five_class.py

# class1:定义金属类
class Metal:
    """
    定义金属类
    静态属性：硬度，光泽，导电性，
    作用：作装饰品，乐器
    """
    def __init__(self, name):
        self.name = name

    def self_introduction(self):
        print(f"hi,我的名字是{self.name}\n")
        print("按下下面的数字，就会了解更多基本信息哦，\n 1.材质硬度\n 2.光泽度\n 3.导电性\n 4.其他的作用\n 0.退出\n")
        while True:
            num_input = input("请在这里输号：")
            try:
                num = int(num_input)
                if num == 1:
                    self.metal_hardness()
                elif num == 2:
                    self.metal_gloss()
                elif num == 3:
                    self.metal_conduct()
                elif num == 4:
                    self.for_decorate()
                    self.for_musical_instruments()
                elif num ==0 :
                    print("成功退出，byebye~~")
                    break
                else:
                    print("这个号跑丢了")
            except:
                print("只能输入int类型的")

    def metal_hardness(self):
        print("金属材质硬度大")

    def metal_gloss(self):
        print("色泽光亮")

    def metal_conduct(self):
        print("可以导电")

    def for_decorate(self):
        print(f"可以用{self.name}来做装饰品")

    def for_musical_instruments(self):
        print(f"在古代，{self.name}被智慧的古代人民用作编钟")


bronze = Metal("bronze")
bronze.self_introduction()

