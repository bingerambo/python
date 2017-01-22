#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: squre-turtle.py
@time: 2016-09-28 10:02
"""


# 前进
def fd(distance):
    print("fd action! and forward distance:", distance)


# 后退
def bk(distance):
    print(" bk action! and back distance:", distance)


# 左转
def lt(t, angle=90):
    if isinstance(t, Turtule):
        print(t.getName(), "turn left!", angle)
    else:
        raise TypeError("it is not Turtule instance")


# 右转
def rt(t, angle=90):
    if isinstance(t, Turtule):
        print(t.getName(), "turn left!", angle)
    else:
        raise TypeError("it is not Turtule instance")


# 乌龟基类
class Turtule():
    def __init__(self):
        print("Turtule init")

    def getName(self):
        return self.__name__

    __name__ = "Turtule"


# 乌龟子类
class XiaoGui(Turtule):
    def __init__(self):
        # super().__init__()
        super(XiaoGui, self).__init__()
        print("XiaoGui init")


# 走方形路线
def square(t, length, angle=90):


    '''
    t：Turtule 对象
    length: 总共步长 非负数
    angle：转弯角度  数字
    '''

    for i in range(4):
        fd(length / 4)
        if i < 3:
            lt(t, angle)

if __name__ == '__main__':
    # t1 = Turtule();
    guigui = XiaoGui()
    # 路线总长度
    len = 600
    square(guigui, len, 45)
