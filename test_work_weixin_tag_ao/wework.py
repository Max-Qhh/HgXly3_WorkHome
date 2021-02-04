# -*- coding: utf-8 -*-
import requests

from test_work_weixin_tag_ao.baseapi import BaseApi


class WeWork(BaseApi):
    """
    用来存放业务的公共步骤，比如获取token
    """

    def __init__(self, secret, corpid):
        self.token = self.get_token(secret, corpid)

    def get_token(self, secret, corpid):
        req = {
            "method": "GET",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": secret,
            }
        }
        r = self.send(req)
        return r.json()['access_token']
