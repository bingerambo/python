#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: tsdl.py
@time: 2016-11-01 15:33
"""

""" 用于文件处理中，对文件头部的预处理
"""
import sys


def skip_header(r):
    """ 用于处理过滤文件的头部描述信息，
        返回待处理的数据内容的第一行
    """
    line = r.readline()
    line = r.readline()

    while line.startswith('#'):
        line = r.readline()
    return line


def process_file(r):
    """ 读取并打印输出流 r
    """
    # 读取数据内容的第一行
    line = skip_header(r).strip()
    print(line)
    # 读取数据内容的剩下内容
    for line in r:
        line = line.strip()
        print(line)


if __name__ == '__main__':
    input_file = open('immoc.txt', 'r')
    process_file(input_file)
    input_file.close()
