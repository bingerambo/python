#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: url_manager.py
@time: 2016-10-27 9:39
"""


class UrlManager(object):
    def __init__(self):
        # 待爬取url集合
        self.new_urls = set()
        # 已爬取url集合
        self.old_urls = set()

    # 添加1个url
    def add_new_url(self, url):
        if url is None:
            return

        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    # 批量添加url
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    # 判断是否有待爬取的url
    def has_new_url(self):
        return len(self.new_urls) != 0

    # 获取待爬取的url
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
