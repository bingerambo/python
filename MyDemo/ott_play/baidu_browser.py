#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: baidu_browser.py
@time: 2016-11-18 16:10
@description:
"""

from splinter import Browser

def fun_browser():

    browser = Browser('firefox')
    browser.visit('http://www.baidu.com')

def test_driver():
    from selenium import webdriver
    import time
    dr = webdriver.Firefox(executable_path='d:/geckodriver')

    time.sleep(5)
    print('Browser will close.')
    dr.quit()
    print('Browser is close')


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    fun_browser()
    # test_driver()