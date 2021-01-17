# -*- coding: utf-8 -*-
"""
打开百度页面
点击登录
弹框中点击‘立即注册’，输入用户名和账号
返回刚才的登录页，点击登录
输入用户名和密码，点击登录
"""
from time import sleep

from selenium import webdriver

from selenium_fram_window.Base import Base


class TestWindows(Base):
    def test_window(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        # 打印窗口
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_link_text("立即注册").click()
        # 再次打印
        print(self.driver.current_window_handle)
        # 打印所有窗口
        print(self.driver.window_handles)
        windows = self.driver.window_handles

        # 窗口切换(选取最后一个窗口)（注册窗口）
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys("不只说声算了")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]').send_keys("18615537012")
        sleep(3)

        # 回到首页，点击登录
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__userName"]').send_keys("不只说声算了")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__password"]').send_keys("mimamimamima")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__submit"]').click()
        sleep(4)