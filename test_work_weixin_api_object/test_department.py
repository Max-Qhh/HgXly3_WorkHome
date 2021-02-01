# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import json

import pytest
import requests
import yaml
from hamcrest import *
# from jsonpath import jsonpath

from test_work_weixin_api_object.department import Department


class TestWeiXin:
    def setup_class(self):
        # 实例化department类，供测试用例调用
        # 传入通讯录的secret
        conf = yaml.safe_load(
            open(r"D:\PycharmProjects\HogWartsXly3\test_work_weixin_api_object\conf.yml"))
        secret = conf["departmentsecret"]
        self.deartment = Department(secret=secret)

    # 创建部门
    # 单接口测试：验证参数是否合法（32位）
    @pytest.mark.parametrize("name,name_en,department_id",
                             [("广州研发中心", "RDGZ", "3"),
                              ("三十二111111111111111111111111111111", "SANER", "4")
                              ]
                             )
    def test_create_department(self, name, name_en, department_id):
        r = self.deartment.create_department(name, name_en, department_id)
        # name部门名称长度大于32，断言错误返回码60001
        if len(name) > 32:
            assert r["errcode"] == 60001
            print("部门长度不符合限制")
        else:
            assert r["errcode"] == 0

    # 更新部门
    @pytest.mark.parametrize("department_id,name,en_name, parentid",
                             [("3", "广州研发中心2", "GZYFLD", "2")
                              ])
    def test_update_department(self, department_id, name, en_name, parentid):
        r = self.deartment.update_department(department_id, name, en_name, parentid)
        r2 = self.deartment.get_department()
        assert r["errmsg"] == "updated"  # 断言更新部门接口是否更新成功

        # 获取部门列表
        print("\njson格式化后的获取部门字典：", json.dumps(r2, ensure_ascii=False))  # 转化为json文件（语法要求是用双引号的）
        print(r2["department"][2]["name"])
        # 问题：数据量大的是时候数据排序没有固定规律，很难取到对应的值
        assert r2["department"][2]["name"] == "广州研发中心2"

        # jsonpath练习
        # print(jsonpath(r2, "$..department[?(@.id==3).name]"))
        # print(jsonpath(r2, "$..department[?(@.name=='广州研发中心2').id]"))
        # print(jsonpath(r2, '$..department[2]'))
        # assert str(jsonpath(r2, '$..department[?(@.id==3)].name')) == "['广州研发中心2']"

        # jsonpath定位断言()
        department_list = self.deartment.jsonpath_req(r2, "$..name")
        department_name = self.deartment.jsonpath_req(r2, "$..department[?(@.id==3)].name")[0]
        print(department_list)
        assert "广州研发中心2" in department_list
        print(department_name)
        assert department_name == "广州研发中心2"

    # 删除部门
    @pytest.mark.parametrize("id",
                             ["3"]
                             )
    def test_delete_department(self, id):
        r = self.deartment.delete_department(id)
        assert r["errmsg"] == "deleted"

    # 获取部门列表
    def test_get_list(self):
        r = self.deartment.get_department()
        print(r)
        # print("所有key值为name的", "\n",
        #       jsonpath(r, '$..name'), "\n")
        # print("key为department对应的value的第一个值", "\n",
        #       jsonpath(r, '$..department[1]'), "\n")
        # print("key为department的所有信息，包含id的字段", "\n",
        #       jsonpath(r, '$..department[?(@.id)]'), "\n")
        # print("key为department的所有信息，id为3的字段", "\n",
        #       jsonpath(r, '$..department[?(@.id==3)]'), "\n")
        # print("key为department的所有信息，id为1的”name“key值", "\n",
        #       jsonpath(r, '$..department[?(@.id==1)].name'), "\n")

    # # 创建标签
    # def test_create_tag(self):
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/create?access_token={self.token}"
    #     data = {
    #         "tagname": "创建标签",
    #         "tagid": 1
    #     }
    #     r = requests.request(method="POST", url=url, json=data)
    #     print(r.json())
    #     assert r.json()['errmsg'] == 'created'
    #
    # # 更新标签名字
    # def test_updata_tag(self):
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/update?access_token={self.token}"
    #     data = {
    #         "tagid": 8,
    #         "tagname": "【领导】"
    #     }
    #     r = requests.request(method="POST", url=url, json=data)
    #     print(r.json())
    #     assert r.json()["errcode"] == 0
    #
    # # 删除标签
    # def test_delete_tag(self):
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/delete?access_token={self.token}"
    #     data = {"tagid": 1}
    #     r = requests.request(method="GET", url=url, params=data)
    #     print(r.json())
    #     assert_that('errmsg' == 'deleted', equal_to('errmsg' == 'deleted'))

    # 获取标签列表
    def test_get_tag_list(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/tag/list?access_token={self.token}"
        r = requests.request(method="GET", url=url)
        l = r.json()
        print(l)
        # print("tag标签名：", jsonpath(r.json(), '$..tagname'), "\n")
