# -*- coding: utf-8 -*-

from typing import List

import pytest
import yaml
import os

# 绝对路径方式一：直接
# with open("D:/PycharmProjects/HogWartsXly3/testing/datas/calc.yml") as f:
# 绝对路径方式二：使用os模块(拿到当前文件所在的路径)
from testing_AllCalc.calc import Calculator

yaml_file_path = os.path.dirname(__file__) + "/datas/calc.yml"
with open(yaml_file_path, encoding='utf-8') as f:
    datas = yaml.safe_load(f)['datas']
    add_datas = datas['add']
    sub_datas = datas['sub']
    mul_datas = datas['mul']
    div_datas = datas['div']
    print(add_datas)
    print(sub_datas)
    print(mul_datas)
    print(div_datas)
    myid = datas['myid']
    print(myid)


@pytest.fixture(params=add_datas, ids=myid)
def get_add_datas(request):
    print("开始测试加法计算")
    data = request.param
    print(f"request.param 里面的测试数据是 {data}")
    yield data
    print("结束加法测试")


@pytest.fixture(params=sub_datas, ids=myid)
def get_sub_datas(request):
    print("开始测试减法计算")
    data = request.param
    print(f"request.param 里面的测试数据是 {data}")
    print(f"测试的结果是 {data[2]}")
    yield data
    print("结束减法计算测试")


@pytest.fixture(params=mul_datas, ids=myid)
def get_mul_datas(request):
    print("开始测试乘法计算")
    data = request.param
    print(f"request.param 里面的测试数据是 {data}")
    yield data
    print("结束测试乘法结算")


@pytest.fixture(params=div_datas, ids=myid)
def get_div_datas(request):
    print("开始测试除法计算")
    data = request.param
    print(f"测试数据是 {data}")
    yield data
    print("结束测试除法结算")


@pytest.fixture(scope="class")
def get_calc():
    print("获取计算器的实例")
    print("开始计算")
    calc = Calculator()
    yield calc
    print("结束计算")


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    """Called after collection has been performed. May filter or re-order
    the items in-place.

    :param pytest.Session session: The pytest session object.
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects.
    """
    # print("items是啥")
    # 收集每个测试用例
    # print(items)
    # 实现用例反转执行(用例会反转执行)
    # items.reverse()

    # 修改测试用例参数编码格式
    # 首先循环item，遍历items列表，每个item拿出来，去修改
    for item in items:
        # 修改用例里的每个name和nodeid的编码格式
        # 通过item.name.nencode把name修改为utf-8（如果说原来是decode unicode-escape的编码格式）
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        # item._nodeid 拿到的是测试用例的名称
        # 自动给测试用例加上标签
        if 'add' in item.nodeid:
            # 将名称传入
            item.add_marker(pytest.mark.add)
        elif 'sub' in item.nodeid:
            item.add_marker(pytest.mark.sub)
        elif 'mul' in item.nodeid:
            item.add_marker(pytest.mark.mul)
        elif 'div' in item.nodeid:
            item.add_marker(pytest.mark.div)
