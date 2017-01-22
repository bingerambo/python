#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: main.py
@time: 2016-11-08 9:40
@description:
"""

# 用于在命令行中执行 python程序
# 把包目录名添加到环境变量中
import sys
import os


# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    # 当前文件路径
    print(__file__)
    # 当前文件目录
    print(os.path.dirname(__file__))
    # 文件绝对目录路径
    curPath = os.path.abspath(os.path.dirname(__file__))
    print(curPath)
    # 上级目录路径
    rootPath = os.path.split(curPath)[0]
    print(rootPath)
    # 添加目录到环境变量，让系统能够搜索到包:MyDemo
    # sys.path.append(rootPath)
