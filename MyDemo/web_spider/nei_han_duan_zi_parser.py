#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: nei_han_duan_zi_parser.py
@time: 2016-11-07 10:30
@description:
"""
from web_spider.lib.html_parser import HtmlParser


class NeiHanTextParser(HtmlParser):
    """ Crawling 'hei han duan zi' text content
        and set crawling data regulation
        example: http://www.qiushibaike.com/text/page/2/?s=4926983
    """

    def parse(self, crawling_url, json_cont, encoding):
        """ 子类的parse处理，自定义相应的解析规则
        """
        # print(json_cont)
        # 通用parse操作，调用基类parse方法，
        # super(NeiHanTextParser, self).parse(crawling_url, html_cont, encoding)

        # new_urls = self.__get_new_urls(crawling_url)
        new_datas = self.__get_new_datas(crawling_url, json_cont)
        return None, new_datas


    def __get_new_datas(self, crawling_url, json_cont):
        """
            json: data:
                    data:
                        group:
                            content

        """
        new_data_group = []
        # contents = self.soup.find('div', id='content').find('div', id='content-left').find_all('div', class_='content')

        contents = json_cont['data']['data']
        if contents is None:
            print("this web page crawling none!")
            return None
        for content in contents:
            new_data_item = {}
            # new_data_item['html_content'] = content
            new_data_item['raw_content'] = content['group']['content'].strip()
            new_data_item['html_content'] = new_data_item['raw_content']
            new_data_group.append(new_data_item)
        return new_data_group


if __name__ == '__main__':
    pass

