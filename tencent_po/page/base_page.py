# -*- coding: utf-8 -*-

# 存放find,find_and_click,等待查找点击,滚动查找,获取toast的text属性
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 定位元素
    def find(self, locator):
        return self.driver.find_element(*locator)

    # 定位并点击
    def find_and_click(self, locator):
        self.find(locator).click()

    # 等待元素可点击并点击
    def wait_for_click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(locator))
        # WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))
        ele = self.driver.find_element(*locator).click()
        return ele

    # 滚动查找并点击
    def find_by_croll_and_click(self, text):
        ele = (MobileBy.ANDROID_UIAUTOMATOR,
               'new UiScrollable(new UiSelector().'
               'scrollable(true).instance(0)).'
               'scrollIntoView(new UiSelector().'
               f'text("{text}").instance(0));')
        self.find_and_click(ele)

    # 获取元素text属性值
    def find_and_get_text(self, locator):
        # 用封装好的find方法查找元素
        return self.find(locator).text
