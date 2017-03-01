#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: group_kaohe.py
@time: 2017-03-01 10:53
@description:
"""

import numpy as np
import pandas as pd
import time

# 考核日期
dates = ['2017-01', '2017-02', '2017-03', '2017-04', '2017-05', '2017-06',
         '2017-07', '2017-08', '2017-09', '2017-10', '2017-11', '2017-12', ]
# 考核人员
name_list = ['gao_fang', 'zhao_wei', 'bin_ge', 'zhang_yuan_fang', 'guo_meng_meng', 'geng_wen_rui', 'wang_han']
# 考核结果表
data = pd.DataFrame(index=pd.to_datetime(dates), columns=name_list)


'''
计算考核的级别
参数：
name_list:考核人员列表
best：优秀 1
normal：一般 -1
其他为0

返回：
rank：考核级别列表
'''
def calc_rank(name_list, best, normal):
    rank = []
    for i in range(len(name_list)):
        # 优秀
        if name_list[i] == best:
            rank.append(1)
        # 一般
        elif name_list[i] == normal:
            rank.append(-1)
        # 其他
        else:
            rank.append(0)
    return rank

'''
计算月度考核的级别
参数：
year_month：考核月份
name_list:考核人员列表
best：优秀 1
normal：一般 -1
其他为0

返回：
data：考核结果表
'''
def calc_month_kaohe(year_month, name_list, best='', normal=''):
    if year_month is None or type(year_month) is not str:
        # 取当前日期
        year_month = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    rank = calc_rank(name_list, best=best, normal=normal)
    print('rank %s ' % rank)
    data.ix[year_month, :] = rank
    return data




'''
执行考核评定
'''
def exec_calc_kaohe():
    # 2017-01
    # best='zhao_wei', normal='wang_bin'
    data = calc_month_kaohe('2017-01', name_list, best='zhao_wei', normal='bin_ge')
    print('data %s ' % data)

    # 2017-02
    # best='zhang_yuan_fang', normal='gao_fang'
    data = calc_month_kaohe('2017-02', name_list, best='zhang_yuan_fang', normal='gao_fang')
    print('data %s ' % data)

    # add kaohe code here

    # 2017-03
    # best='zhang_yuan_fang', normal='gao_fang'

if __name__ == '__main__':
    exec_calc_kaohe()

    # 以下为功能测试所用
    # data2 = data.bin_ge[data.bin_ge.notnull()]
    # print(data2)
    # print(data.fillna(0))