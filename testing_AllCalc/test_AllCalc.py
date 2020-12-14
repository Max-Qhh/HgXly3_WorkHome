# -*- coding: utf-8 -*-
"""
补全计算器（加减乘除）的测试用例
使用数据的数据驱动，完成加减乘除用例的自动生成
创建 fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
控制测试用例顺序按照【加-减-乘-除】这个顺序执行
结合allure 生成测试结果报告
"""
import allure
import pytest


@allure.feature("测试计算器")
class TestCalc:

    # 加法
    @pytest.mark.add
    @pytest.mark.run(order=1)
    @allure.story("测试加法")
    def test_add(self, get_calc, get_add_datas):
        # 因为作用域的问题，定义None，获取result，和断言对比
        result = None
        # 异常处理
        try:
            with allure.step("计算两个数的相加和"):
                result = get_calc.add(get_add_datas[0], get_add_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)

        # 得到结果之后，需要写断言
        assert result == get_add_datas[2]

    # @pytest.mark.add
    # @allure.story("测试加法（自定义测试数据）")
    # def test_add2(self, get_calc):
    #     result = get_calc.add(0.1, 0.2)
    #     assert round(result, 2) == 0.3

    # @pytest.mark.sub
    # @allure.story("测试减法")
    # def test_sub(self):
    #     print("test_sub")
    #
    # @pytest.mark.mul
    # @allure.story("测试乘法")
    # def test_mul(self):
    #     print("test_mul")
    #
    # @pytest.mark.div
    # @allure.story("测试除法")
    # def test_div(self):
    #     print("test_div")

    # 减法
    @pytest.mark.sub
    @allure.story("测试减法")
    @pytest.mark.run(order=2)
    def test_sub(self, get_calc, get_sub_datas):
        result = None
        try:
            with allure.step("计算两个数相减"):
                result = get_calc.sub(get_sub_datas[0], get_sub_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)

        assert result == get_sub_datas[2]

    # 乘法
    @pytest.mark.mul
    @pytest.mark.run(order=3)
    @allure.story("测试乘法")
    def test_mul(self, get_calc, get_mul_datas):
        result = None
        try:
            with allure.step("计算两个数相乘"):
                result = get_calc.mul(get_mul_datas[0], get_mul_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)

        assert result == get_mul_datas[2]

    # 除法
    @pytest.mark.div
    @pytest.mark.run(order=4)
    @allure.story("测试除法")
    def test_div(self, get_calc, get_div_datas):
        result = None
        try:
            with allure.step("测试两个数相除"):
                result = get_calc.div(get_div_datas[0], get_div_datas[1])
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)

        assert result == get_div_datas[2]
