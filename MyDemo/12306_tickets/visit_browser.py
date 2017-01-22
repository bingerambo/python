#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: visit_browser.py
@time: 2016-11-18 16:10
@description:
"""
import os
import traceback

from splinter import Browser

from time import sleep


class VistConfig(object):
    def __init__(self):
        """网址配置信息"""
        self.ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
        self.login_url = "https://kyfw.12306.cn/otn/login/init"
        self.init_my_url = "https://kyfw.12306.cn/otn/index/initMy12306"


class UserConfig(object):
    def __init__(self):
        """登录用户信息"""
        self.name = "feibinge"
        self.psw = "501344wb"


class InfoConfig(object):
    def __init__(self):
        """登录用户信息"""
        self.fromStation = "%u90D1%u5DDE%2CZZF"
        self.fromDate = "2016-11-21"
        self.toStation = "%u897F%u5B89%u5317%2CEAY"
        self.passengers = ["赵巍"]
        self.order = 2


def login(browser):
    """ 登录配置
    """
    user_info = UserConfig()
    # 登录
    browser.find_by_text(u"登录").click()
    browser.fill('loginUserDTO.user_name', user_info.name)
    browser.fill('userDTO.password', user_info.psw)


def login_process():
    # 需要登录
    while browser.is_text_present(u'登录'):
        login(browser)
        sleep(1)
        print(u"等待验证码输入......")

        while True:
            # 登录完成
            if browser.url == config.init_my_url:
                return


def query_ticket():
    """ 设置查询车票信息
    """
    set_cookie_info(browser)

    browser.visit(config.ticket_url)


def polling_reserve():
    """ 轮询列表所有车次，进行订票
    """
    count = 0
    while browser.url == config.ticket_url:

        # 查询
        browser.find_by_text(u"查询").click()
        sleep(1)
        # 轮询订票
        count += 1
        print(u"循环列表，点击查询... 第 %s 次" % count)

        try:
            for yu_ding in browser.find_by_text(u"预订"):
                yu_ding.click()
        except:
            print(u'第%d个车次车票，现在无法预订，继续轮询订票...' % count)
            continue


def order_reserve(order):
    """ 指定序号，进行订票
        order : 指定序号，第一个为1，依次如：2，3，4，5...
    """
    count = 0
    while browser.url == config.ticket_url:
        browser.find_by_id('query_ticket').click()
        sleep(1)
        # 指定订票
        count += 1
        print(u"指定序号，点击查询... 第 %s 次" % count)

        try:
            browser.find_by_text(u"预订")[order - 1].click()
        except:
            print(u'第%d个车次车票，现在无法预订... 准备尝试第%d次预订' % (order, count + 1))
            continue


def conform_passenger():
    """ 乘客信息确认，选择乘客，并确认
    """
    print(u'进入订票乘客信息页面...')
    login_user = browser.find_by_id('login_user').value
    # print("login user id: " + login_user)

    for name in info.passengers:
        if name == login_user:
            # 登录用户 选取元素的索引值为1
            browser.find_by_text(name)[1].click()
        else:
            browser.find_by_text(name)[0].click()
        print(u'已选择乘客：%s' % name)


def reserve_ticket():
    """ 订票处理操作
    """
    order = info.order

    if order > 0:
        order_reserve(order)
    elif order == 0:
        polling_reserve()
    else:
        print("订票order有误，请检查order值是否为非负数")


def vist_url():
    global browser

    browser = Browser(driver_name="chrome")

    browser.visit(config.ticket_url)

    try:
        login_process()
        query_ticket()
        reserve_ticket()
        conform_passenger()

        print('恭喜你，车票预订成功！！！')

    except Exception as e:
        print(traceback.print_exc())


def set_cookie_info(browser):
    # 添加出发地
    browser.cookies.add({"_jc_save_fromStation": info.fromStation})

    # 添加出发日期
    browser.cookies.add({"_jc_save_fromDate": info.fromDate})

    # 添加目的地
    browser.cookies.add({'_jc_save_toStation': info.toStation})

    b_cookie = browser.cookies.all()
    print(b_cookie)


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    config = VistConfig()
    info = InfoConfig()
    vist_url()
