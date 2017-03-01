#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: numpy_array.py
@time: 2017-02-15 15:42
@description:
"""

import numpy as np

data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)

print(arr1)
print(arr1.shape, arr1.ndim, arr1.dtype)
print(arr2)
print(arr2.shape, arr2.ndim, arr2.dtype)

"""
数组广播、索引
"""
arr1_2mi = arr1 * arr1
print(arr1_2mi)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print [7, 8, 9]
print(arr2d[2])
# print 3
print(arr2d[0][2])
print(arr2d[0, 2])

# 多维数组切片
# 注意下面两个操作的差异
# 只有冒号:表示选取了整个轴
print(arr2d[:, :1])
# print(arr2d[:,0])

# 布尔型索引
names = np.array(['bob', 'will', 'tom', 'jack', 'dick', 'bill', 'tom'])
# print(names)
data_name = np.random.randn(7, 4)
print(data_name)

print(names == 'tom')
print(data_name[names == 'tom'])

print(data_name[names == 'tom', :2])
print(data_name[names == 'tom', 3])

data_name_old = data_name.copy()
data_name[data_name < 0] = 0
print(data_name)
data_name = data_name_old
print(data_name)

# 花式索引 利用整数数组 进行索引
arr_hua = np.empty((8, 4))
for i in range(8):
    arr_hua[i] = i
print(arr_hua)

arr_hua[[-3, -5]]
print(arr_hua[[4, 3, 0, 6]])
print(arr_hua[[-3, -5]])

# 数组转置和轴对换
print('==============')
print('数组转置和轴对换')
arr_trans = np.arange(15).reshape(3, 5)
print(arr_trans)
print(arr_trans.T)

# 随机漫步
print('==============')
print('随机漫步')
nsteps = 1000

draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()
print(walk)
print(walk.min())
print(walk.max())
print(np.abs(walk) > 10)

# 多个随机漫步
print('==============')
print('多个随机漫步')
nwalks = 5000
nsteps = 1000

draws = np.random.randint(0, 2, size=(nwalks, nsteps))  # 0或者1
steps = np.where(draws > 0, 1, -1)
print(steps)
print(steps.shape)
walks = steps.cumsum(1)
print(walks)
print(walks.min())
print(walks.max())
hist30 = (np.abs(walks) > 30)
print('hist30====')
print(hist30)
print('hist30.any(1)====')
print(hist30.any(1))

# 达到30以上的数量
hist30_num = sum(hist30)
print(hist30_num)

# 获取穿越时间
print("# 获取穿越时间")
crossing_times = (np.abs(walks) > 30).argmax(1)
print(crossing_times)
# 穿越时间均值
print(crossing_times.mean(), len(crossing_times))
