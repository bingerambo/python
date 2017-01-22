#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: spider_main.py
@time: 2016-11-02 9:31
@description:
"""

# 用于在命令行中执行 python程序
# 把包目录名添加到环境变量中
# import sys
# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)


import time
from datetime import datetime


class SpiderMain():
    def __init__(self):

        from web_spider.lib import url_manager
        self.urls = url_manager.UrlManager()
        from web_spider.lib import html_downloader
        self.downloader = html_downloader.HtmlDownloader()
        from web_spider import text_parser
        self.parser = text_parser.Text_HtmlParser()
        from web_spider.lib import html_outputer
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url, crawling_name_tag, output_file_name):
        """ 爬虫执行程序
            root_url: 入口起始url
            crawling_name_tag：生成文件的标题
            output_file_name: 生成文件的名称
        """
        # run time statistic
        start_time = 0
        try:
            if root_url is None or root_url == "":
                raise ValueError('root_url is not none or ""')
            # crawling counter number
            count = 0
            success_count = 0
            failed_count = 0

            # The start time
            start_time = time.clock()

            self.urls.add_new_url(root_url)

            while self.urls.has_new_url():
                try:
                    crawling_url = self.urls.get_new_url()

                    print("crawling %d web page, url: %s" % (count + 1, crawling_url))

                    self.downloader.download(crawling_url)

                    # print(html_cont)

                    new_urls, new_data_group = self.parser.parse(crawling_url, self.downloader.html_cont,
                                                                 self.downloader.encoding)

                    success_count = success_count + 1
                except Exception as e:
                    failed_count = failed_count + 1
                    print("Uh! crawling the %d web page failed!" % count)
                finally:
                    self.outputer.collect_data(new_data_group)
                    self.urls.add_new_urls(new_urls)
                    count = count + 1

                    # 休眠500毫秒，避免出现 服务器502 Bad Gateway
                    time.sleep(0.5)

            print("Wow! crawling complete! And crawling pages information:")
            print("total: %d , success: %d , failure: %d " % (count, success_count, failed_count))
            # print(self.outputer.datas)
            self.outputer.output_html(crawling_name_tag, output_file_name)
        except Exception as e:
            print(e)
            print("Oh! crawling failed!")
        finally:
            # The end time
            end_time = time.clock()
            print("The run time is : %.03f seconds" % (end_time - start_time))


class NeiHanSpider(SpiderMain):
    def __init__(self):
        super(NeiHanSpider, self).__init__()
        from web_spider.lib import json_downloader
        self.downloader = json_downloader.JsonDownloader()
        from web_spider import nei_han_duan_zi_parser
        self.parser = nei_han_duan_zi_parser.NeiHanTextParser()
        # 爬取总页数设置
        self.TOTAL_NUM = 1000

    def crawl(self, root_url, crawling_name_tag, output_file_name):
        """ 爬虫执行程序
            root_url: 入口起始url
            crawling_name_tag：生成文件的标题
            output_file_name: 生成文件的名称
        """
        # run time statistic
        start_time = 0
        try:
            if root_url is None or root_url == "":
                raise ValueError('root_url is not none or ""')
            # crawling counter number
            count = 0
            success_count = 0
            failed_count = 0

            # The start time
            start_time = time.clock()

            self.urls.add_new_url(root_url)
            # 根据目标站点获取，并设置headers信息
            cookies, headers = self.get_headers_info()

            while self.urls.has_new_url():
                try:

                    crawling_url = root_url + self.get_time_stamp(count)

                    print("crawling %d web page, url: %s" % (count + 1, crawling_url))

                    self.downloader.download(crawling_url, cookies=cookies, headers=headers)

                    new_urls, new_data_group = self.parser.parse(crawling_url, self.downloader.json_cont,
                                                                 self.downloader.encoding)

                    success_count = success_count + 1
                except Exception as e:
                    failed_count = failed_count + 1
                    print(e)
                    print("Uh! crawling the %d web page failed!" % count)
                finally:
                    self.outputer.collect_data(new_data_group)
                    # self.urls.add_new_urls(new_urls)
                    count = count + 1

                    # 完成设置页数，结束爬取
                    if success_count == self.TOTAL_NUM:
                        break

                    # 休眠500毫秒，避免出现 服务器502 Bad Gateway
                    time.sleep(0.5)

            print("Wow! crawling complete! And crawling pages information:")
            print("total: %d , success: %d , failure: %d " % (count, success_count, failed_count))
            # print(self.outputer.datas)
            self.outputer.output_html(crawling_name_tag, output_file_name)
        except Exception as e:
            print(e)
            print("Oh! crawling failed!")
        finally:
            # The end time
            end_time = time.clock()
            print("The run time is : %.03f seconds" % (end_time - start_time))

    def get_headers_info(self):
        """ 获取目标站点保存客户端的cookie参数信息,并设置headers信息
        """
        # 目标站点起始url
        home_url = "http://neihanshequ.com"
        self.downloader.initial_request(home_url)

        # 自定义cookie、headers信息
        cookies_req = self.downloader.cookies
        cookies = {}
        cookies['Hm_lvt_773f1a5aa45c642cf87eef671e4d3f6a'] = '1478135330, 1478135332, 1478485644, 1478485687'
        cookies['Hm_lpvt_773f1a5aa45c642cf87eef671e4d3f6a'] = '1478485687'
        cookies['uuid'] = cookies_req['uuid']
        cookies['tt_webid'] = cookies_req['tt_webid']
        cookies['csrftoken'] = cookies_req['csrftoken']

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
            'Connection': 'keep-alive',
            'X-CSRFToken': cookies['csrftoken']
        }
        return cookies, headers

    def get_time_stamp(self, count):
        """ 取得10位时间戳, 每次请求递减，用于请求不同页面
            count：已爬页面数量
        """
        # var_bias为步长
        if count == 0:
            # 起始为当前时间戳
            var_bias = 0
        else:
            var_bias = 15000 * count
        int_bias_stamp = int(datetime.now().timestamp() - var_bias)
        str_stamp = '%d' % int_bias_stamp
        return str_stamp


if __name__ == '__main__':
    spider_main = SpiderMain()
    root_url = "http://www.qiushibaike.com/text/"
    spider_main.crawl(root_url, "小段子-Binge", "小段子-Binge-2017-01-20.html")


    # nei_han = NeiHanSpider()
    # neihan_duanzi_url = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&has_more=True&max_time="
    #
    # nei_han.crawl(neihan_duanzi_url, "内涵-小段子-Binge", "小段子-Binge-2017-01-20.html")
