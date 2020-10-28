# -*- coding:utf-8 -*-
# @time    :2020/10/28 16:40
# @Author  :dmingzhu
# @dmingzhu:math_demo.py

class CalculateDemo:
    def multiply(self, a, b):
        return a*b

    def division(self, a, b):
        return a/b



if __name__ == "__main__":
    cc = CalculateDemo()
    aa = cc.division(1, 3)
    # aa = cc.multiply(0.0006, 0.000002)
    print(aa)

