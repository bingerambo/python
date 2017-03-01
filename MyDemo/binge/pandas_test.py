#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: pandas_test.py
@time: 2017-02-16 15:31
@description:
"""
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Series
obj = Series([4, 7, -5, 3])
print(obj)
print("values: %s, index: %s" % (obj.values, obj.index))

obj2 = Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
print(obj2)

print(obj2['a'])
print(obj2['c'])

'b' in obj2  # True
print('b' in obj2)

print(np.exp(obj2))
obj22 = obj2[obj2 > 0]
obj22 = obj2 * 2

print(obj2[obj2 > 0])
print(obj22)
print('obj2 series 没受到影响 *2')
print(obj2)

# dict -> Series
print('##############')
print('dict -> Series')
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utath': 5000}
obj3 = Series(sdata)
print(obj3)

states = ['Ohio ',
          'Oregon',
          'Texas',
          'Utath'
          ]
obj4 = Series(sdata, index=states)
print(obj4)
print(pd.isnull(obj4))
print(pd.notnull(obj4))

print(obj3 + obj4)

# DataFrame 表格型数据结构
# 含有一组有序的列，每列可有不同的值类型：数值，字符串， 布尔值
# 既有行索引也有列索引，可以看做由Series组成的字典（共用一个索引）

print('##############')
print('DataFrame 表格型数据结构')

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
print(frame)
# 指定列索引序列
frame_col = DataFrame(data, columns=['year', 'state', 'pop'])
print(frame_col)

# 指定列索引，行索引序列
frame_col_index = DataFrame(data, columns=['year', 'state', 'pop'],
                            index=['one', 'two', 'three', 'four', 'five'])
print(frame_col_index)

print(frame_col_index.columns)
print(frame_col_index.year)  # 这是个series
print(frame_col_index.year.two)
if 'three' in frame_col_index.year:
    print(frame_col_index.year['three'])
# 获取索引
print('############')
print('获取索引')
# 获取第一行
print(frame_col_index.ix['one'])
# 获取one行的state列
# print(frame_col_index.ix['one']['state'])
print(frame_col_index.ix['one'].state)

# 获取year列的第一行
print(frame_col_index.year.ix['one'])

# 为不存在的列赋值，新建生成新的列
frame_col_index['eastern'] = frame_col_index.state == 'Ohio'
print(frame_col_index)

# 获取前2行数据
print('获取前2行数据')
print(frame_col_index[:2])

# 删除某列
del frame_col_index['eastern']
print(frame_col_index)

# 重新索引行
print('重新索引行')
frame_reindex = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],
                          columns=['Ohio', 'Texas', 'California'])
print(frame_reindex)

frame_reindex_2 = frame_reindex.reindex(['a', 'b', 'c', 'd'])
print(frame_reindex_2)

states = ['Ohio', 'Utah', 'California']
frame_reindex_2 = frame_reindex.reindex(columns=states)
print(frame_reindex_2)

frame_reindex_3 = frame_reindex.reindex(index=['a', 'b', 'c', 'd'], method='ffill', columns=states)
print(frame_reindex_3)
# 排序
series_te = frame_reindex_3['Ohio'].sort_values()
series_te = frame_reindex_3['Ohio'].sort_values(ascending=False)
print(series_te)


# DataFrame 和 Series 之间的运算
print('DataFrame 和 Series 之间的运算')
arr = np.arange(12.).reshape((3,4))
print(arr)
arr0 = arr[0]
arr2 = arr - arr0
print(arr2)



# 滤除缺失数据
from numpy import nan as NA
data_que = Series([1,NA,3.6,NA,7])
print(data_que.dropna())


# 层次化索引
print('层次化索引')
data_many_layer = Series(np.random.randn(10), index=[['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,2,3]])

print(data_many_layer)
print(data_many_layer.index)

print(data_many_layer['b'])
print(data_many_layer['b':'c'])
print(data_many_layer.ix[['b','c']])
print(data_many_layer[:,2])
# 层次索引-数据重塑和分组操作
# unstack() 把Series转DataFrame
print(data_many_layer.unstack())
print(data_many_layer.unstack().T)
# stack() 把DataFrame转Series
print(data_many_layer.unstack().stack())















if __name__ == '__main__':
    pass
