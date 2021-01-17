# -*- coding: utf-8 -*-
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_js.Base import Base


class TestJs(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")

        # 调用js的代码块(使用它的返回值)（加上return！）
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        time.sleep(3)

        # 根据自己的需要，使用for循环打印js脚本得到的结果，可以都执行，第二种办法只返回了一个title的结果。注意哦！！
        # for code in [
        #     'return document.title', 'return JSON.stringify(performance.timing)'
        # ]:
        #     print(self.driver.execute_script(code))
        print(self.driver.execute_script("return document.title; return JSON.stringify(performance.timing)"))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")

        # 方法一：移除readonly方法属性(测试发现不用移除属性)
        # time_element =self.driver.execute_script(
        #     "a=document.getElementById('train_date');a.removeAttribute('readonly')")
        # 方法二：
        # self.driver.execute_script("return removeAttribute('readonly')")
        # 方法三（设置方法）：
        # time_element = "a=document.getElementById('train_date');a.removeAttribute('readonly')"
        # self.driver.execute_script(time_element)
        # time.sleep(3)
        # self.driver.execute_script("document.getElementById('train_date').value='2020-12-30'")

        # 对元素赋值（使用直接强制等待）
        # time.sleep(5)
        # self.driver.execute_script("document.getElementById('train_date').value='2020-12-29'")

        # 使用显示等待方法一，找到元素可被点击并赋值
        # def wait(x):
        #     return len(self.driver.find_elements(By.ID, "train_date")) >= 1
        #
        # WebDriverWait(self.driver, 20).until(wait)
        # self.driver.execute_script("document.getElementById('train_date').value='2020-12-28'")

        # 使用显示等待方法二，直到元素可被点击
        local = (By.ID, "train_date")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(local)
        )
        self.driver.execute_script("document.getElementById('train_date').value='2020-12-29'")

        # 获得属性
        print(self.driver.find_element_by_id("train_date").get_attribute("value"))
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
        time.sleep(3)
