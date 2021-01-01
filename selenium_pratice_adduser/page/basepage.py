# -*- coding: utf-8 -*-

# 初始化drivre，进行封装
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, base_url: WebDriver = None):
        # 变量名后面的冒号是：类型注解,标识。这里WebDriver就是base_url期望的类型
        # 避免driver重复初始化
        if base_url is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
        else:
            self.driver = base_url

    # :的意思是给一个注解，by传一个定位方式，locator传一个字符串，封装find
    def find(self, by: WebDriver, locator: str):
        return self.driver.find_element(by, locator)

    def finds(self, by: WebDriver, locator: str):
        return self.driver.find_elements(by, locator)

    # timeout默认十秒，也可以到通讯录page去设置
    def wait_for_click(self, locator, timeout=10):
        element: WebDriver = WebDriverWait(self.driver, timeout).until\
            (expected_conditions.element_to_be_clickable(locator))
        return element
