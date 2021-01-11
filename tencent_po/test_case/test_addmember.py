# -*- coding: utf-8 -*-
import os
from time import sleep

import pytest
import yaml
from hamcrest import *

from tencent_po.page.app import App


def get_data():
    yaml_file_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r"\data\memberlist.yml"
    with open(yaml_file_path)as f:
        data = yaml.safe_load(f)['data']
        addmemberlist = data["add"]
        return addmemberlist
        # print(addmemberlist)


class TestAddMember:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize("name, gender, phonenm, email", get_data())
    def test_add_contact(self, name, gender, phonenm, email):
        toast = self.main.click_addresslist().add_member().addconect_menual(). \
            edit_name(name).edit_genter(gender).edit_phonenm(phonenm).edit_email(email).\
            edit_save().get_toast()

        # assert "添加成功" == toast
        # print("添加成功")
        assert_that(toast, equal_to('添加成功'))
        print("添加成功")

    @pytest.mark.skip
    def test_clickaddresslist(self):
        self.main.click_addresslist()
