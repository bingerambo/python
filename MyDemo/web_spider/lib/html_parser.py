#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: html_parser.py
@time: 2016-11-02 9:39
@description:
"""

from bs4 import BeautifulSoup


class HtmlParser(object):
    def __init__(self):
        self.soup = None

    def parse(self, crawling_url, html_cont, encoding):
        """ 基类的parse处理，统一通过html.parser 解析到-> soup中
        """

        self.soup = BeautifulSoup(html_cont, 'html.parser', from_encoding=encoding)
        if self.soup.original_encoding != encoding.swapcase():
            print("soup.original_encoding: %s and response encoding: %s is not the same" % (
                self.soup.original_encoding, encoding))
            # print(self.soup.prettify('utf-8'))
            # print(self.soup.title.string.strip())

    def __get_new_urls(self, crawling_url):
        new_urls = set()
        pass
        return new_urls

    def __get_new_datas(self, crawling_url):
        new_datas = {}
        pass
        return new_datas


if __name__ == '__main__':
    # HtmlParser().parse("", html_doc, 'utf-8')
    pass
