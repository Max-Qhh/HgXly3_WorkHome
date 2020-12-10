# -*- coding: utf-8 -*-
import pytest
import yaml

from python_pratice.TestCalcProject.calc import Calculator

with open("D:/PycharmProjects/HogWartsXly3/python_pratice/TestCalcProject/datas/calc.yml") as f:
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


class TestCalc:

    def setup_class(self):
        print("开始测试")
        # 实例化计算器类（不推荐全局）
        self.ca = Calculator()

    def teardown_class(self):
        print("测试结束")

    def setup(self):
        print("开始测试该用例")

    def teardown(self):
        print("该用例测试结束")

    @pytest.mark.parametrize(
        "a, b, expect",
        add_datas,
        # yaml文件中有四组值
        # ids=['int', 'float', 'round', 'fail', 'negative']
        ids=myid
    )
    # expect预期结果
    def test_add(self, a, b, expect):
        # 实例化计算器类
        # calc = Calculator()
        # 调用add方法
        result = self.ca.add(a, b)
        # 判断result类型是浮点，做出保留两位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，需要写断言
        assert result == expect

    # 减法
    @pytest.mark.parametrize(
        "a, b, expect",
        sub_datas,
        ids=myid
    )
    def test_sub(self, a, b, expect):
        result = self.ca.sub(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    # 乘法
    @pytest.mark.parametrize(
        "a, b, expect",
        mul_datas,
        ids=myid
    )
    def test_mul(self, a, b, expect):
        result = self.ca.mul(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    # 除法
    @pytest.mark.parametrize(
        "a, b, expect",
        div_datas,
        ids=myid
    )
    def test_div(self, a, b, expect):
        result = self.ca.div(a, b)
        if isinstance(result, float):
            result = round(result, 2)
        assert result == expect

    # def test_add2(self):
    #     result = self.ca.add(0.1, 0.2)
    #     # 通过round保留两位小数
    #     assert round(result, 2) == 0.3

    # def test_add1(self):
    #     # 调用add方法
    #     result = self.ca.add(0.1, 0.1)
    #     assert result == 0.2
    #
    # def test_add2(self):
    #     # 调用add方法
    #     result = self.ca.add(-1, -1)
    #     assert result == -2
