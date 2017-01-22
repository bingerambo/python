#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: html_downloader.py
@time: 2016-11-02 9:39
@description:
"""
from web_spider.lib import request_emitter


class HtmlDownloader(object):
    def __init__(self):
        self.request = request_emitter.RequestEmitter()
        self.html_cont = None
        self.encoding = None

    def get_html_cont(self, response, *args, **kwargs):
        """ request的钩子函数
        """
        print("状态码:", response.status_code, response.reason)
        print("编码信息:", response.encoding)

        self.html_cont = response.content
        self.encoding = response.encoding

    def download(self, crawling_url):
        try:
            if crawling_url is None or crawling_url == "":
                raise ValueError('crawling_url is not none or ""')
            self.request.get_request(crawling_url, self.get_html_cont)
        except Exception as e:
            print(e)
        else:
            return self.html_cont


if __name__ == '__main__':
    pass
# downloader = HtmlDownloader()
# root_url = "http://www.qiushibaike.com/text/"
# downloader.download(root_url)
