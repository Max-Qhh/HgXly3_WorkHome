# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import json

import allure
import pytest
import yaml
from hamcrest import *

from test_work_weixin_tag_ao.tag import Tag


@allure.feature("通讯录管理-标签管理")
class TestWeiXin:
    def setup_class(self):
        # 实例化department类，供测试用例调用
        # 传入通讯录的secret
        conf = yaml.safe_load(
            open(r"D:\PycharmProjects\HogWartsXly3\test_work_weixin_tag_ao\conf.yml"))
        secret = conf["tag"]
        corpid = conf["corpid"]
        self.tag = Tag(secret=secret, corpid=corpid)

    # @pytest.mark.parametrize("tagname,tagid",
    #                          [
    #                              # ("行政", "7"),
    #                              # ("销售", "6"),
    #                              # ("研发", "5")
    #                              ("323232323232323232323232323232323", "12")
    #                          ]
    #                          )
    @allure.story("创建标签测试用例")
    @allure.title("创建标签")
    @pytest.mark.tag
    @pytest.mark.run(order=1)
    def test_create_tag_fixture(self, create_tag):
        # print(reate_tag[0],create_tag[1])
        r = self.tag.create_tag(create_tag[0], create_tag[1])
        assert r.status_code == 200
        print(r.json())
        if len(create_tag[0]) > 32:
            # assert r["errcode"] == 40058
            assert self.tag.jsonpath_req(r.json(), "$..errcode")[0] == 40058
            print(f"当前标签名称长度为{len(create_tag[0])}，超出32个字符要求")
        else:
            assert self.tag.jsonpath_req(r.json(), "$..errmsg")[0] == "created"

    # @pytest.mark.parametrize("tagid,tagname",
    #                          [("7", "【行政】")
    #
    #                           ]
    #                          )
    @allure.story("更新标签名字")
    @allure.title("更新标签名字")
    @pytest.mark.run(order=2)
    def test_updata_tag(self, update_tag):
        r = self.tag.update_tag(update_tag[0], update_tag[1])
        assert r["errcode"] == 0

    # @pytest.mark.parametrize("tagid",
    #                          ["7"]
    #                          )
    @allure.story("删除标签")
    @allure.title("删除标签")
    @pytest.mark.run(order=5)
    def test_delete_tag(self, delete_tag):
        r = self.tag.delete_tag(delete_tag)
        print(r)
        assert_that('errmsg' == 'deleted', equal_to('errmsg' == 'deleted'))
        assert self.tag.jsonpath_req(r, "$..errmsg")[0] == "deleted"

    # @pytest.mark.parametrize("tagid",
    #                          [("7")]
    #                          )
    @allure.story("获取标签成员")
    @allure.title("获取标签成员")
    @pytest.mark.run(order=6)
    def test_get_tag_user(self, get_tag_user):
        r = self.tag.get_tag_user(get_tag_user)
        print(f"\n获取标签id为{get_tag_user}的成员： ", self.tag.jsonpath_req(r, "$..name"))

    # @pytest.mark.parametrize("tagid,userlist,partylist",
    #                          [("7", ['app-user1', 'app-user2'], [])
    #                           # [("8", [], ['2'])
    #                           ])
    @allure.story("增加标签成员")
    @allure.title("增加标签成员")
    @pytest.mark.run(order=3)
    def test_create_tag_user(self, create_tag_user):
        r = self.tag.create_tag_user(create_tag_user[0], create_tag_user[1], create_tag_user[2])
        print(r)
        assert self.tag.jsonpath_req(r, "$..errcode")[0] == 0

    # @pytest.mark.parametrize("tagid,userlist,partylist",
    #                          [("7", ['app-user1', 'app-user2'], [])
    #                           # [("8", [], ['2'])
    #                           ])
    @allure.story("删除标签成员")
    @allure.title("删除标签成员")
    @pytest.mark.run(order=4)
    def test_delete_tag_user(self, delete_tag_user):
        r = self.tag.delete_tag_user(delete_tag_user[0], delete_tag_user[1], delete_tag_user[2])
        print(r)
        assert self.tag.jsonpath_req(r, "$..errmsg")[0] == "deleted"

    @allure.story("获取标签列表")
    @allure.title("获取标签列表")
    @allure.description("查看最终的标签列表")
    @allure.severity("trivial")
    @pytest.mark.run(order=7)
    def test_get_tag_list(self):
        with allure.step("1: 打印最终的标签列表"):
            r = self.tag.get_tag_list()
            print("获取标签列表：", self.tag.jsonpath_req(r, '$..tagname'), "\n")
        with allure.step("2: 检验结果"):
            allure.attach('标签列表打印成功', '期望结果')
            allure.attach('标签列表打印成功', '实际结果')
