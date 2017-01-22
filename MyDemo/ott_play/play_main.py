#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: play_main.py
@time: 2016-10-31 15:27
"""
# 用于在命令行中执行 python程序
# 把包目录名添加到环境变量中
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

"""该文件为 双向系统第三方业务集成接口测试，
    如：可用于模拟客户端调用接口进行播控
"""
# 请求消息URL
rq_url = "http://172.30.93.225:8080/spgw"
# 点播鉴权
rq_data = dict(
    attribute='json_ott_play',
    csi='12001047',
    stamp=0,
    productId='PT20150306155806815',
    assetId='VODC1608241254085401',
    tgt='TGT-566225753-YYoRcifKCkLljncB6LHbtY2PGIDYf4oprRV7NXbv4AGvzCeqIS-cas',
    startPoint='0'

)
# 鉴权
order_data = dict(
    attribute='json_order_prod',
    csi='12001047',
    stamp=0,
    productId='PT20150306155806815',
    # assetId='VODC1608241254085401',
    tgt='TGT-566225753-YYoRcifKCkLljncB6LHbtY2PGIDYf4oprRV7NXbv4AGvzCeqIS-cas',
    startPoint='0'

)
# 点播记录
cdr_data = dict(
    attribute='json_get_cdr',
    # attribute='json_get_batchcdr',
    csi='12001047',
    stamp=0,
    # productId='PT20150306155806815',
    # assetId='VODC1608241254085401',
    tgt='TGT-566225753-YYoRcifKCkLljncB6LHbtY2PGIDYf4oprRV7NXbv4AGvzCeqIS-cas',
    # startPoint='0'
    starttime="2015-10-01 12:00:00",
    endtime="2016-11-02 12:00:00"

)

# 置换tvn
getTvn_data = dict(
    attribute='json_gettvn',
    # attribute='json_get_userinfo',
    csi='12001047',
    stamp=0,
    tgt='TGT-566225753-YYoRcifKCkLljncB6LHbtY2PGIDYf4oprRV7NXbv4AGvzCeqIS-cas'
)
# 获取用户归属区域码和TVN
getGeoTvn_data = dict(
    attribute='json_get_tvnandldcbytvn',
    csi='12001047',
    stamp=0,
    tgt='TGT-566225753-YYoRcifKCkLljncB6LHbtY2PGIDYf4oprRV7NXbv4AGvzCeqIS-cas'
)


def get_key_info(response, *args, **kwargs):
    """ 发送消息后，hook函数，需自定义
    """
    print("状态码，说明:", response.status_code, response.reason)
    print("头部信息:", response.headers)

    print("URL 信息:", response.url)
    print("redirect 信息:", response.history)
    print("耗费时长:", response.elapsed)
    print("request 信息:", response.request.method)
    print('----------------------')
    print("编码信息:", response.encoding)
    print("消息主体内容: byte:", response.content, type(response.content))
    print("消息主体内容: 解析:", response.text, type(response.text))
    # print("消息主体内容:", response.json(), type(response.json()))
    print('----------------------')
    # 使用response 内置的json解析
    json_data = response.json()
    # print("json解析：", json_data)
    # print('获得的点播链接地址：')
    # print(json_data['DataArea']['url'])


# 块打印，区分打印内容
def chunk_header_print(str_name):
    print()
    print("**********************")
    print(str_name)
    print('-----------')


# 客户端发送请求消息-程序入口
class Main():
    def __init__(self, data):
        from ott_play import play_params
        self.play_params = play_params.PlayParams(data)
        from ott_play import request_emitter
        self.request = request_emitter.RequestEmitter()

    def send_get_params(self, url):
        self.play_params.set_params()
        request_params = self.play_params.get_params()
        self.request.params_request(url, request_params, get_key_info)


if __name__ == '__main__':
    chunk_header_print("点播鉴权信息")
    main_ott_play = Main(rq_data)
    main_ott_play.send_get_params(rq_url)

    # chunk_header_print("产品订购信息")
    # main_ott_order = Main(order_data)
    # main_ott_order.send_get_params(rq_url)

    chunk_header_print("点播记录信息")
    main_ott_cdr = Main(cdr_data)
    main_ott_cdr.send_get_params(rq_url)

    chunk_header_print("置换TVN信息")
    main_ott_cdr = Main(getTvn_data)
    main_ott_cdr.send_get_params(rq_url)

    chunk_header_print("获取用户归属区域码和TVN信息")
    main_ott_cdr = Main(getGeoTvn_data)
    main_ott_cdr.send_get_params(rq_url)

