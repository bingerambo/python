#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: Binge
@file: spider_main.py
@time: 2016-10-27 9:35
"""

from baike_spider import url_manager
from baike_spider import html_downloader
from baike_spider import html_parser
from baike_spider import html_outputer


class SpiderMain(object):
    def __init__(self):

        self.urls = url_manager.UrlManager()

        self.downloader = html_downloader.HtmlDownloader()

        self.parser = html_parser.HtmlParser()

        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        # 爬取计数
        count = 1

        self.urls.add_new_url(root_url)

        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()

                print("正在爬取第 %d 个网页： URL链接：%s" % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)

                print("爬取中***********")
                # print(new_data['title'])
                # print(type(new_data['summary']))

                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    print("已经爬取1000个页面，完成！！！")
                    break
                count = count + 1
            except:
                print("craw fail: 爬取失败")

        # 爬取数据页面输出
        self.outputer.output_html()


if __name__ == '__main__':
    # print("spider main run")
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    # print(type(obj_spider.urls))
