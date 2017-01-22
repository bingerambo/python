#!/usr/bin/env python
# encoding: utf-8



"""
@version: ??
@author: binge
@file: request_emitter.py
@time: 2016/10/30 20:18
@description:   进行http消息发送和处理，
                引用requests包
"""

import requests


def download_image(response, *args, **kwargs):
    """回调函数
    """
    print("状态码，说明:", response.status_code, response.reason)
    print("头部信息:", response.headers)

    with open('demo.jpg', 'wb') as fd:
        # 每128写入一次
        for chunk in response.iter_content(128):
            fd.write(chunk)


class RequestEmitter(object):
    """ get请求消息
        call_back 为钩子函数名
    """

    # get请求消息
    # call_back 为钩子函数名
    def get_request(self, url, call_back=None):
        try:
            response = requests.get(url, hooks=dict(response=call_back), timeout=20)
            response.raise_for_status()
        except Exception as e:
            print(e)

    def params_request(self, url, params, call_back):
        """ get带参数请求消息
            params为参数字典，call_back 为钩子函数名
        """
        try:
            response = requests.get(url, params=params, hooks=dict(response=call_back), timeout=20)
            response.raise_for_status()
        except Exception as e:
            print(e)

    def get_custom_request(self, url, call_back, **kwargs):
        """ get消息 定制请求头headers 和 cookies
            为请求添加 HTTP 头部，只要简单地传递一个 dict 给 headers 参数就可以了
        """
        try:
            if ('cookies' not in kwargs and 'headers' not in kwargs):
                response = requests.get(url, hooks=dict(response=call_back), timeout=20)
            elif ('cookies' in kwargs and 'headers' not in kwargs):
                response = requests.get(url, hooks=dict(response=call_back), cookies=kwargs['cookies'], timeout=20)
            elif ('cookies' not in kwargs and 'headers' in kwargs):
                response = requests.get(url, headers=kwargs['headers'], hooks=dict(response=call_back), timeout=20)
            elif ('cookies' in kwargs and 'headers' in kwargs):
                response = requests.get(url, headers=kwargs['headers'], hooks=dict(response=call_back),
                                        cookies=kwargs['cookies'], timeout=20)
            response.raise_for_status()
        except Exception as e:
            print(e)

    def post_request(self, url, json_data, call_back):
        """ post消息 分 json 和 data 两种
            call_back 为钩子函数名
        """
        try:
            response = requests.post(url, auth=('imoocdemo', 'imoocdemo123'),
                                     json=json_data,
                                     hooks=dict(response=call_back), timeout=100)
            # response = requests.post(url, auth=('imoocdemo', 'imoocdemo123'), data=data,
            #                          hooks=dict(response=call_back), timeout=100)
            response.raise_for_status()
        except Exception as e:
            print(e)

    def custom_requests(slef, url, headers):
        """ 自定义request消息,修改消息头
        """
        from requests import Request, Session
        s = Session()
        # headers = {'User-Agent': 'fake-binge'}
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        # req = Request('GET', build_uri('user/emails'), auth=('imoocdemo', 'imoocdemo123'), headers=headers)
        req = Request('GET', url, auth=('imoocdemo', 'imoocdemo123'), headers=headers)

        prepared = req.prepare()
        # print(prepared.headers)
        # print(prepared.body)

        try:
            response = s.send(prepared, timeout=100)
            response.raise_for_status()
        except Exception as e:
            print(e)
        else:
            print(response.status_code)
            print(response.request.headers)
            print(response.text)

    def stream_request(self, url, call_back):
        """ 载文件、图片等流文件请求消息
            call_back 为钩子函数名
        """
        try:
            # 构造头信息
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            # 流开关打开 对于此版本，是否构造消息头部和打开流开关，都可以下载文件
            # response = requests.get(url, headers=headers, stream=True, hooks=dict(response=call_back), timeout=10)
            # response = requests.get(url, hooks=dict(response=call_back), timeout=10)
            from contextlib import closing
            with closing(requests.get(url, headers=headers, stream=True, hooks=dict(response=call_back), timeout=10)
                         ) as response:
                response.raise_for_status()

        except Exception as e:
            print(e)

    # @staticmethod
    def get_key_info(self, response, *args, **kwargs):
        """回调函数
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
        # print("消息主体内容 JSON->DICT:", response.json(), type(response.json()))


if __name__ == '__main__':
    pass

    # req_emitter = RequestEmitter()
    # for i in range(1):
    #     print('start %d times request' % (i + 1))
    #     req_emitter.get_request(URL, get_key_info)
    # img_url = "http://h.hiphotos.baidu.com/image/pic/item/f9dcd100baa1cd11dd1855cebd12c8fcc2ce2db5.jpg"
    # req_emitter.stream_request(img_url, download_image)

    # for i in range(1):
    #     print('start %d times param request' % (i + 1))
    #     req_emitter.params_request(build_uri('users'), {'since': 20}, get_key_info)
    #     req_emitter.post_request(build_uri('user/emails'), ['helloworld-feifei@github.com'], get_key_info)
    #     req_emitter.custom_requests()
