#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: json_downloader.py
@time: 2016-11-07 9:40
@description:
"""
from web_spider.lib import request_emitter


class JsonDownloader(object):
    def __init__(self):
        self.request = request_emitter.RequestEmitter()
        self.json_cont = None
        self.encoding = None
        self.cookies = None

    def get_json_cont(self, response, *args, **kwargs):
        """ request的钩子函数
        """
        print("状态码:", response.status_code, response.reason)
        print("编码信息:", response.encoding)
        # print("响应-头部信息:", response.headers)
        # print("请求-头部信息:", response.request.headers)

        self.json_cont = response.json()
        self.encoding = response.encoding

    def download(self, crawling_url, **kwargs):
        try:
            if crawling_url is None or crawling_url == "":
                raise ValueError('crawling_url is not none or ""')
            self.request.get_custom_request(crawling_url, self.get_json_cont, **kwargs)
        except Exception as e:
            print(e)
        else:
            return self.json_cont

    def initial_request(self, url):
        def hooks_func(resp, *args, **kwargs):
            self.cookies = resp.cookies

        self.request.get_request(url, hooks_func)


if __name__ == '__main__':
    pass
