#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: test_web_api.py
@time: 2016-11-01 17:14
@description: 测试web http api接口
"""

from ott_play import request_emitter


def get_key_info(response, *args, **kwargs):
    """回调函数
    """
    print("状态码，说明:", response.status_code, response.reason)
    print("头部信息:", response.headers)

    print("URL 信息:", response.url)
    print("redirect 信息:", response.history)
    print("耗费时长:", response.elapsed)
    print("request 信息:", response.request.method)
    print('----------------------')

    # print("编码信息:", response.encoding)
    sss = response.content

    # print("消息主体内容: byte:", response.content, type(response.content))
    # print("消息主体内容: 解析:", response.text, type(response.text))
    # print("消息主体内容 JSON->DICT:", response.json(), type(response.json()))

class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    zw_url = "http://10.63.62.177:8080/ZwHttpInterface/ZwGetAssetInfo?assetId=VODC1512231056229401"
    request = request_emitter.RequestEmitter()
    # get_key_info = request.get_key_info
    # zhaowei api
    #     request.get_request(zw_url, get_key_info)

    # 新乡社保接口
    # request.get_request("http://172.30.65.147:8080/hncatvservice/xxYiBao/login.do?username=13938460134&password=123456", get_key_info)

    # 鹤壁投票接口
    request.get_request("http://172.30.96.166/navigate.ashx?name=HBvote&PGT=TGT-577394547-YbBnYjcSVkd15Iwfelas23sG0xOhYXdDWSm1nhkvRKVgJlUwJK-cas", get_key_info)

    # # 内涵段子
    # neihan_duanzi_url   = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time="
    # # neihan_duanzi_url_2 = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1478135170.8"
    # # neihan_duanzi_url_3 = "http://neihanshequ.com/joke/?is_json=1&app_name=neihanshequ_web&max_time=1478135161.8"
    # #
    # request.get_request(neihan_duanzi_url, get_key_info)
    # # time.sleep(1)
    # # print("------------------------------")
    # # request.get_request(neihan_duanzi_url_3, get_key_info)
    #
    # def func(resp, *args, **kwargs):
    #     print(resp.cookies)
    #     for name in resp.cookies:
    #         print(name)
    #     print(resp.cookies['uuid'])
    # neihan_home_url= "http://neihanshequ.com/"
    # resp = request.get_request(neihan_home_url, func)