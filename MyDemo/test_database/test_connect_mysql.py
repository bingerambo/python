#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: test_connect_mysql.py
@time: 2016-10-28 10:43
"""
import pymysql

# host = '127.0.0.1',
# port = 3306,
# user = 'root',
# passwd = 'root',
# db = 'mysql',
# charset = 'utf8'

# 连接配置信息
mysql_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'db': 't2',
    'charset': 'utf8'
}

# 创建链接
conn = pymysql.Connect(**mysql_config)

cursor = conn.cursor()

sql = "select * from tb1"

cursor.execute(sql)
print(cursor.rowcount)

# print(cursor.fetchone())
# print(cursor.fetchmany(2))
# print(cursor.fetchall())

rs = cursor.fetchall()

for username, age, salary in rs:
    print("username:", username, "age:", age, "salary", salary)

# print(conn)
# print(conn.host_info)
# print(cursor)

cursor.close()
conn.close()

if __name__ == '__main__':
    pass
