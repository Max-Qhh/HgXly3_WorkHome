# -*- coding: utf-8 -*-

# 底层通用技术
import requests
from jsonpath import jsonpath


class BaseApi:
    def send(self, req):
        return requests.request(**req)

    def jsonpath_req(self, obj, expr):
        return jsonpath(obj, expr)
