#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: transfer_money.py
@time: 2016-10-28 14:27
"""

# 连接配置信息
import sys

import pymysql

# MySQL默认的存储引擎是MyISAM，MyISAM存储引擎不支持事务处理，
# 所以改变autocommit没有什么作用。但不会报错，
# 所以要使用事务处理的童鞋一定要确定你所操作的表示支持事务处理的，
# 如InnoDB。如果不知道表的存储引擎可以通过查看建表语句,
# 查看建表的时候有没有指定事务类型的存储引擎，
# 如果没有指定存储引擎默认则是MyISAM不支持事务的存储引擎。
# 当然，事务处理是为了保障表数据原子性、一致性、隔离性、持久性。
# 这些都是要消耗系统资源的，要谨慎选择。

# 数据库连接配置
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'passwd': 'root',
    'db': 'account',
    'charset': 'utf8'
}


class TransferMoney(object):
    def __init__(self, conn):
        self.conn = conn

    def transfer(self, source_accid, target_accid, money):
        # try块中 是一个事务
        try:
            self.check_acct_available(source_accid)
            self.check_acct_available(target_accid)
            self.has_enough_money(source_accid, money)
            self.reduce_money(source_accid, money)
            # self.add_money(target_accid, money)

            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise e

    def check_acct_available(self, accid):
        cursor = self.conn.cursor()
        try:
            sql = "select accid from acc_tb where accid=%s" % accid
            cursor.execute(sql)
            print("check_acct_available:", sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号%s不存在" % accid)
        finally:
            cursor.close()

    def has_enough_money(self, accid, money):
        cursor = self.conn.cursor()
        try:
            sql = "select accid from acc_tb where accid=%s and money>%s " % (accid, money)
            cursor.execute(sql)
            print("has_enough_money:", sql)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号%s余额不足" % accid)

        finally:
            cursor.close()

    def reduce_money(self, accid, money):
        cursor = self.conn.cursor()
        try:
            sql = "update acc_tb set money=money-%s where accid=%s" % (money, accid)
            # print(sql)
            cursor.execute(sql)
            print("reduce_money:", sql)
            # 注意update操作结果的验证方法
            if cursor.rowcount != 1:
                raise Exception("账号%s减款失败", accid)

        finally:
            cursor.close()

    def add_money(self, accid, money):
        cursor = self.conn.cursor
        try:
            sql = "update acc_tb set money=money-%s where accid=%s" % (money, accid)
            cursor.execute(sql)
            print("add_money:", sql)
            # 注意update操作结果的验证方法
            if cursor.rowcount != 1:
                raise Exception("账号%s加款失败", accid)
        except Exception as e:
            raise e
        finally:
            cursor.close()


if __name__ == '__main__':
    # source_accid = sys.argv[1]
    # target_accid = sys.argv[2]
    # money = sys.argv[3]

    source_accid = 11
    target_accid = 12
    money = 100

    conn = pymysql.Connect(**config)
    # print(conn.host_info)
    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_accid, target_accid, money)
    except Exception as e:
        print("出现了问题：", e)
    finally:
        conn.close()
