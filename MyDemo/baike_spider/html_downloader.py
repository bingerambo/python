#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: Binge
@file: html_downloader.py
@time: 2016-10-27 9:41
"""
import urllib.request

# 下载器
class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
