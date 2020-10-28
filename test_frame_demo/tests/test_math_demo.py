# -*- coding:utf-8 -*-
# @time    :2020/10/28 16:48
# @Author  :dmingzhu
# @dmingzhu:test_math_demo.py
import pytest
import allure
@allure.feature("两数相乘")
class TestMultiply:

    @allure.story("同为正整数")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (3, 4, 12)
                             ])
    def test_mul_1(self, a, b, c):
        assert a*b == c

    @allure.story("同为负整数")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (-3, -4, 12)
                             ])
    def test_mul_2(self, a, b, c):
        assert a*b == c

    @allure.story("一正一负整数")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (3, -4, -12)
                             ])
    def test_mul_3(self, a, b, c):
        assert a*b == c

    @allure.story("同为正数，且小数位数小于等于2")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (0.06, 0.02, 0.0012),
                                 (0.4, 0.6, 0.24),
                                 (0.3, 0.05, 0.015)
                             ])
    def test_mul_4(self, a, b, c):
        assert a*b == c

    @allure.story("同为正数，且小数位数大于2")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (0.003, 0.003, 0.000009),
                                 (0.02, 0.0003, 0.000006)
                             ])
    def test_mul_5(self, a, b, c):
        assert a*b == c

    @allure.story("同为负数，且小数位数小于等于2")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (-0.03, -0.04, 0.0012),
                                 (-0.1, -0.01, 0.0001)
                             ])
    def test_mul_6(self, a, b, c):
        assert a*b == c

    @allure.story("同为负数，且小数位数大于2")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (-0.003, -0.004, 0.000012),
                                 (-0.001, -0.01, 0.00001)
                             ])
    def test_mul_7(self, a, b, c):
        assert a*b == c

    @allure.story("一正一负，且小数位数小于等于2")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (-0.03, 0.04, -0.0012),
                                 (-0.1, 0.01, -0.001),
                                 (-1.2, 0.9, -1.08),
                                 (48563.20, -0.52, -25252.864)
                             ])
    def test_mul_8(self, a, b, c):
        assert a*b == c

    @allure.story("一正一负，且小数位数大于2")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (-0.003, 0.004, -0.000012),
                                 (-0.1, 0.001, -0.0001),
                                 (-1.123, 0.457, -0.513211),
                                 (48563.20, -0.2352, -11422.06464)
                             ])
    def test_mul_9(self, a, b, c):
        assert a*b == c

    @allure.story("包含0")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (0, 0.004, 0),
                                 (-0.1, 0, 0),
                                 (0, 0, 0)
                             ])
    def test_mul_10(self, a, b, c):
        assert a*b == c

    @allure.story("包含字符")
    @pytest.mark.parametrize("a, b",
                             [
                                 ("aa", "bb"),
                                 (2, "aa"),
                                 ("@#", 4),
                                 ("乘法", 5)
                             ])
    def test_mul_11(self, a, b):
        with pytest.raises(Exception):
            assert type(a) == int or float
            assert type(b) == int or float


    @allure.story("包含None")
    @pytest.mark.parametrize("a, b",
                             [
                                 (None, 2)
                             ])
    def test_mul_12(self, a, b):
        with pytest.raises(Exception):
            assert type(a) == int or float

    @allure.story("包含True")
    @pytest.mark.parametrize("a, b",
                             [
                                 (True, 2)
                             ])
    def test_mul_13(self, a, b):
        with pytest.raises(Exception):
            assert type(a) == int or float


@allure.feature("两数相除")
class TestDivision:

    @allure.story("同为正整数")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (3, 400, 0.0075)
                                     ])
    def test_div_1(self, a, b, c):
        assert a/b == c


    @allure.story("同为负整数")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (-3, -4, 0.75)
                             ])
    def test_div_2(self, a, b, c):
        assert a/b == c

    @allure.story("一正一负整数")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (30, -40, -0.75)
                             ])
    def test_div_3(self, a, b, c):
        assert a/b == c

    @allure.story("同为正数，小数")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (0.06, 0.02, 3),
                                 (0.3, 0.05, 6)
                             ])
    def test_div_4(self, a, b, c):
        assert a/b == c



    @allure.story("同为负数，小数")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (-0.03, -0.04, 0.75),
                                 (-0.1, -0.01, 10)
                             ])
    def test_div_5(self, a, b, c):
        assert a/b == c


    @allure.story("一正一负，小数")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (-0.03, 0.04, -0.75),
                                 (-0.1, 0.01, -10)
                             ])
    def test_div_6(self, a, b, c):
        assert a/b == c

    @allure.story("商为无限小数")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (1, 3, 0.0013333333333333333333333)
                             ])
    def test_div_7(self, a, b, c):
        assert a/b == c


    @allure.story("被除数为0")
    @pytest.mark.parametrize("a, b, c",
                             [
                                 (0, 0.04, 0),
                                 (0, -0.01, 0)
                             ])
    def test_div_8(self, a, b, c):
        assert a/b == c

    @allure.story("除数为0")
    @pytest.mark.parametrize("a, b",
                             [
                                 (1000, 0),
                                 (-0.1, 0)
                             ])
    def test_div_9(self, a, b):
        if b == 0:
            raise ZeroDivisionError

    @allure.story("包含字符")
    @pytest.mark.parametrize("a, b",
                             [
                                 ("aa", "bb"),
                                 (2, "aa"),
                                 ("@#", 4),
                                 ("乘法", 5)
                             ])
    def test_div_10(self, a, b):
        with pytest.raises(Exception):
            assert type(a) == int or float
            assert type(b) == int or float


    @allure.story("包含None")
    @pytest.mark.parametrize("a, b",
                             [
                                 (None, 2)
                             ])
    def test_div_11(self, a, b):
        with pytest.raises(Exception):
            assert type(a) == int or float

    @allure.story("包含True")
    @pytest.mark.parametrize("a, b",
                             [
                                 (True, 2)
                             ])
    def test_div_12(self, a, b):
        with pytest.raises(Exception):
            assert type(a) == int or float