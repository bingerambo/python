#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: text_parser.py
@time: 2016-11-07 9:15
@description:
"""
import urllib

from web_spider.lib.html_parser import HtmlParser


class Text_HtmlParser(HtmlParser):
    """ Crawling qiushi text content
        and set crawling data regulation
        example: http://www.qiushibaike.com/text/page/2/?s=4926983
    """

    def parse(self, crawling_url, html_cont, encoding):
        """ 子类的parse处理，自定义相应的解析规则
        """

        # 通用parse操作，调用基类parse方法，
        super(Text_HtmlParser, self).parse(crawling_url, html_cont, encoding)

        new_urls = self.__get_new_urls(crawling_url)
        new_datas = self.__get_new_datas(crawling_url)
        return new_urls, new_datas

    def __get_new_urls(self, crawling_url):
        new_urls = set()

        # <ul class="pagination"><li><a href="/text/page/2?s=4926902" rel="nofollow"><span class="next">下一页</span></a></li></ul>

        next_span = self.soup.find('ul', class_='pagination').find('span', class_='next')

        if next_span is None:
            print("crawling the last web page, will end!")
            return None

        # link = next_span.parent
        new_url = next_span.parent['href']
        new_full_url = urllib.parse.urljoin(crawling_url, new_url)
        # print(new_full_url)
        new_urls.add(new_full_url)
        return new_urls

    def __get_new_datas(self, crawling_url):
        new_data_group = []
        contents = self.soup.find('div', id='content').find('div', id='content-left').find_all('div', class_='content')

        if contents is None:
            print("this web page crawling none!")
            return None
        for content in contents:
            # print(content)
            new_data_item = {}
            new_data_item['html_content'] = content
            new_data_item['raw_content'] = content.get_text().strip()
            new_data_group.append(new_data_item)

        return new_data_group

if __name__ == '__main__':
    pass