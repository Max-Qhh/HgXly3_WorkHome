# -*- coding: utf-8 -*-

#
import os

import pytest
import yaml

from selenium_pratice_adduser.page.main_page import MainPage


yaml_file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"\datas\member.yaml"
# yaml_file_path = r".\datas\member.yaml"
with open(yaml_file_path)as g:
# with open("D:/PycharmProjects/HogWartsXly3/selenium_pratice_adduser/datas/member.yaml")as f:
    data = yaml.safe_load(g)['data']
    ymlcy = data['ymlcy']
def test_yam():
    print(g)

class TestLogin:

    def setup(self):
        # 调用main对象，做实例化
        self.main = MainPage()

    def teardwon(self):
        pass

    # 测试用例
    @pytest.mark.parametrize("name,id,mail", [("赵五", "1225CYzw", "chengyuanzw@qq.com")])
    def test_login(self, name, id, mail):
        # name = "张三"
        # id = "1225CYzs"
        # mail = "chengyuanzs@qq.com"

        # 主页调用通讯录界面，点击添加成员，再添加成员，再回到通讯录界面调用getmember(断言)
        namelist = self.main.goto_contact_page().click_add_member(). \
            add_member(name, id, mail).get_member()
        print(namelist)
        # assert "成员F" in namelist
        assert name in namelist

    @pytest.mark.parametrize("name,id,mail", [
        ("首页添加1", "1225sytj1", "sytj1@qq.com")
    ])
    def test_login1(self, name, id, mail):
        # name = "首页添加1"
        # id = "1225sytj1"
        # mail = "1225sytj1"
        namelist_1 = self.main.goto_add_member_page().add_member(name, id, mail).get_member()
        print(namelist_1)
        assert name in namelist_1

    @pytest.mark.parametrize("name,id,mail", ymlcy)
    def test_login2(self, name, id, mail):
        namelist_2 = self.main.goto_contact_page().click_add_member(). \
            add_member(name, id, mail).get_member()
        print(namelist_2)
        assert name in namelist_2
