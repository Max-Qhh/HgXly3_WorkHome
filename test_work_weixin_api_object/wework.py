# -*- coding: utf-8 -*-
import requests

from test_work_weixin_api_object.baseapi import BaseApi


class WeWork(BaseApi):
    """
    用来存放业务的公共步骤，比如获取token
    """

    def __init__(self, secret):
        # 创建哪一个类变量，通过调用self.get_token()函数，获取到token信息
        self.token = self.get_token(secret)

    def get_token(self, secret):
        # 获取corp_id和corp_secret
        req = {
            "method": "GET",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": "ww85e92f9f0b5746ff",
                "corpsecret": secret,
            }
        }
        r = self.send(req)
        return r.json()['access_token']
