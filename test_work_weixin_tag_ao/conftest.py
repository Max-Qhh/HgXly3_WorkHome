# -*- coding: utf-8 -*-
import os

import pytest
import yaml

yaml_file_path = os.path.dirname(__file__) + "./data.yml"
with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)["tagmanage"]

    create_tag = datas["create_tag"]
    create_tag_id = datas["create_tag_id"]

    update_tag = datas["update_tag"]

    delete_tag = datas["delete_tag"]

    get_tag_user = datas["get_tag_user"]

    create_tag_user = datas["create_tag_user"]

    delete_tag_user = datas["delete_tag_user"]

    get_tag_list = datas["get_tag_list"]


# 添加标签
@pytest.fixture(params=create_tag, scope='function')
def create_tag(request):
    data = request.param
    yield data
    print("添加标签测试用例执行结束")


# 添加标签ids数据
@pytest.fixture(params=create_tag_id)
def creat_tag_id(request):
    data = request.param
    yield data


# 更新标签数据
@pytest.fixture(params=update_tag)
def update_tag(request):
    data = request.param
    yield data


# 删除标签数据
@pytest.fixture(params=delete_tag)
def delete_tag(request):
    data = request.param
    yield data


# 获取标签成员数据
@pytest.fixture(params=get_tag_user)
def get_tag_user(request):
    data = request.param
    yield data


# 创建标签成员数据
@pytest.fixture(params=create_tag_user)
def create_tag_user(request):
    data = request.param
    yield data


# 删除标签成员数据
@pytest.fixture(params=delete_tag_user)
def delete_tag_user(request):
    data = request.param
    yield data


# 获取标签列表数据
@pytest.fixture(params=get_tag_list)
def get_tag_list(request):
    data = request.param
    yield data
