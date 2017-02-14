#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@version: ??
@author: Binge
@file: ott_play_params.py
@time: 2016-10-31 15:32
"""
from datetime import datetime


# rq_data = dict(
#     rq_url="http://172.30.93.225:8080/spgw",
#     attribute='json_ott_play',
#     csi='12001047',
#     stamp=0,
#     productId='PT20150306155806815',
#     assetId='VODC1608241254085401',
#     tgt='TGT-563424232-DLaIBm3l24YFhwSrS2NztzOqbnf4VJnI5kMtusuhaRKqMshkZM-cas',
#
#
# )

# # 双向认证接口
# params = dict(
#     rq_url="http://172.30.93.225:8080/spgw",
#     attribute='json_gettvn',
#     csi='12001047',
#     stamp=0,
#     tgt="TGT-15900-1Rcni2IIK1SmFPDHV7wmyhGnw70se3C9wfJs6LcD3HvNdJLGAL-cas"
# )

class GetReqParams(object):
    def __init__(self, data):
        self.request_data = data

    def set_params(self):
        # 设置 stmap、cseq
        time_stamp = self.get_time_stamp()
        self.request_data['stamp'] = time_stamp
        self.request_data['cseq'] = time_stamp
        # 设置token md5串
        self.request_data['token'] = self.get_token()

    def get_time_stamp(self):
        # 取得毫秒级 13位时间戳
        str_stamp = '%d' % int(datetime.now().timestamp() * 1000)
        return str_stamp

    def get_token(self):
        from ott_play import md5_lib
        try:
            # salt-key
            # csi + "_" + secretKey + '_' + timestamp
            csi = self.request_data['csi']
            secret_key = csi
            timestamp = self.request_data['stamp']
            str_salt = csi + '_' + secret_key + '_' + timestamp

            return md5_lib.Md5Lib().get_md5(str_salt)
        except Exception as e:
            print(e)

    def get_params(self):
        return self.request_data


if __name__ == '__main__':
    pass
    # play_params = OttPlayParams(rq_data)
    # play_params.set_params()
    #
    #
    # print(rq_data)
    # print(play_params.request_data)
