# -*- coding: utf-8 -*-
import pytest
import requests
from hamcrest import *


class TestWeiXin:
    def setup_class(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        # 获取corp_id和corp_secret
        params = {
            "corpid": "corpid",
            "corpsecret": "corpsecret",
        }
        r = requests.request(method="GET", url=url, params=params)
        self.token = r.json()['access_token']
        self.err = r.json()
        # 出错返回码
        assert r.json()["errcode"] == 0

    def test_demo(self):
        print(self.err)

    # 创建部门
    @pytest.mark.skip
    def test_create_department(self):
        # 请求地址
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create"
        # 请求包体
        data = {
            "name": "广州研发中心",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1,
            "id": 2
        }
        params = {"access_token": self.token}
        r = requests.request(method="POST", url=url, params=params, json=data)
        assert r.json()["errcode"] == 0

    # 更新部门
    @pytest.mark.skip
    def test_update_department(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        data = {
            "id": 2,
            "name": "广州研发中心更新",
            "name_en": "RDGZ",
            "parentid": 1,
            "order": 1
        }
        r = requests.request(method="POST", url=url, json=data)
        print(r.json())
        assert r.json()["errmsg"] == "updated"

    # 删除部门
    @pytest.mark.skip
    def test_delete_department(self):
        id = 2
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id={id}"
        r = requests.request(method="GET", url=url)
        assert r.json()["errmsg"] == "deleted"

    # 获取部门列表
    def test_get_list(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}"
        r = requests.request(method="GET", url=url)
        print(r.json())

    # 创建标签
    def test_create_tag(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
        data = {
            "tagname": "创建标签",
            "tagid": 1
        }
        r = requests.request(method="POST", url=url, json=data)
        print(r.json())
        assert r.json()['errmsg'] == 'created'

    # 更新标签名字
    def test_updata_tag(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
        data = {
            "tagid": 8,
            "tagname": "【领导】"
        }
        r = requests.request(method="POST", url=url, json=data)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 删除标签
    def test_delete_tag(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}"
        data = {"tagid": 1}
        r = requests.request(method="GET", url=url, params=data)
        print(r.json())
        assert_that('errmsg' == 'deleted', equal_to('errmsg' == 'deleted'))

    # 获取标签列表
    def test_get_tag_list(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        r = requests.request(method="GET", url=url)
        list = r.json()['taglist']
        print(list)