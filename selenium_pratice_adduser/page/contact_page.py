# -*- coding: utf-8 -*-

# 通讯录界面
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium_pratice_adduser.page.basepage import BasePage


class ContactPage(BasePage):
    # 点击添加成员
    def click_add_member(self):
        from selenium_pratice_adduser.page.add_member_page import AddMemberPage
        # 等待“添加成员”元素
        ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
        # 显式等待，等待元素是可点击状态
        # WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(ele))
        # 调用basepage的显示等待,5自定义显示等待时间
        self.wait_for_click(ele, 5)

        # 解决点击无效问题；设置死循环多次点击，直到目标元素出现后，跳出死循环
        while True:
            # *是解数组
            # self.driver.find_element(*ele).click()
            self.find(By.CSS_SELECTOR, ".ww_operationBar .js_add_member").click()
            # element = self.driver.find_elements_by_id('username')
            # finds用来打印列表
            element = self.finds(By.ID, "username")
            if len(element) > 0:
                break
        # 面向对象
        return AddMemberPage(self.driver)

    # 断言
    def get_member(self):
        time.sleep(1)
        # eles = self.driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
        eles = self.finds(By.CSS_SELECTOR,".member_colRight_memberTable_td:nth-child(2)")
        name_list = []
        for value in eles:
            # 获取元素属性title的值，存入list内
            print(value.get_attribute("title"))
            name_list.append(value.get_attribute("title"))
        # 断言目标名字是否在列表内
        # assert "成员C" in name_list
        return name_list
