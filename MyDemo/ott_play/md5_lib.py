#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: md5_lib.py
@time: 2016-10-31 16:44
"""
import hashlib


class Md5Lib(object):
    def get_md5(self, str_salt):
        if str_salt is None or str_salt == '':
            # print("Md5Lib.get_md5 异常：MD5加密串为空")
            # return
            raise ValueError("Md5Lib.get_md5 异常：MD5加密串为空")

        md5 = hashlib.md5()
        md5.update(str_salt.encode('utf-8'))
        # print(md5.hexdigest())
        # 此处系统要求 md5串为大写
        return md5.hexdigest().upper()



if __name__ == '__main__':
    md5lib = Md5Lib()
    sss = md5lib.get_md5('michael')
    print(sss)

