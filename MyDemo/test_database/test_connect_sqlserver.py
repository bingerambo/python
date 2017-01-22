#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: test_connect_sqlserver.py
@time: 2016-10-28 16:12
"""
import pymssql

"""使用pymssql连接sqlserver数据库，验证测试，配置参数名和连接函数名有不同
"""

# 连接配置信息
sqlserver_config = {
    'host': '10.63.70.164',
    'port': 1433,
    'user': 'sa',
    'password': 'hncatv123',
    'database': 'test',
    'charset': 'utf8'
}


def sqlServerLink():
    # 创建链接
    conn = pymssql.connect(**sqlserver_config)
    cursor = conn.cursor()
    print(conn)
    print(cursor)
    try:
        sql = "select * from test_tab"
        cursor.execute(sql)
        print("sqlServerLink:", sql)
        rs = cursor.fetchall()
        for row in rs:
            print(row)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    sqlServerLink()
