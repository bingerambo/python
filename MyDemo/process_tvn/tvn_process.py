#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
@version: 0.1
@author: Binge
@file: tvn_process.py
@time: 2016-09-30 14:21
@description: 用来按导航系统规定TVN格式
    整理文档："12345678,23456789,96385274..."
    1.默认TVN源文件名称：tvn.txt，文件路径为当前目录
    2.默认生成目标文件名称：tvn_data.txt,文件路径为当前目录
        每次执行会覆盖原有目标文件
"""

__author__ = "Binge"

import string


def process_line(line, content):
    """ 处理每行字符串 加入内容列表中
        line: str 每行字符串
        content: list 待添加的内容列表
    """
    list_in_line = line.split()
    list_new_line = []
    for item in list_in_line:
        item = item.strip(string.punctuation + string.whitespace)
        list_new_line.append(item)
    content.extend(list_new_line)


def process_content(content):
    """ 把content列表转字符串，用","分隔
        content: list 待处理转换的内容列表
        return: str 字符串
    """
    return ",".join(content)


def process_file(src_file_name="./TVN/中州路7#街坊-TVN号-1229.txt", dest_file_name="./TVN/中州路7#街坊-TVN号-1229-data.txt"):
    """ 整理文件操作
        src_file_name：str 源文件
        dest_file_name：str 目标文件
    """
    # if type(src_file_name) != str or type(dest_file_name) != str:
    #     print("输入的文件名称类型不对！！！")
    #     return False

    f_src = open(src_file_name, 'r', encoding='utf-8', errors='ignore')
    f_dest = open(dest_file_name, "w", encoding="utf-8")
    # TVN数据缓存列表
    content = []
    iter_f = iter(f_src)

    for line in iter_f:
        process_line(line, content)

    # 按格式整理TVN数据，并写入目标文件
    f_dest.write(process_content(content))
    print("TVN 个数：", len(content))

    # 关闭文件
    f_src.close()
    f_dest.close()


if __name__ == '__main__':
    process_file()
