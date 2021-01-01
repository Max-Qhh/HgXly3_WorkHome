# -*- coding: utf-8 -*-

# 添加成员界面，断言
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_pratice_adduser.page.basepage import BasePage
from selenium_pratice_adduser.page.contact_page import ContactPage


class AddMemberPage(BasePage):
    # 完善添加成员,ID元素改变好只需修改此处，便于维护
    # po中的细节不可以暴露在外，从公共方法提供给web
    # 在变量前加私有属性，编码规范
    _ele_name = (By.ID, "username")
    _ele_id = (By.ID, "memberAdd_acctid")
    _ele_mail = (By.ID, "memberAdd_mail")

    # 输入信息
    def add_member(self, name, id, mail):
        # *解元祖
        self.find(*self._ele_name).send_keys(name)
        self.find(*self._ele_id).send_keys(id)
        self.find(*self._ele_mail).send_keys(mail)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        # 最后要到通讯录界面断言
        return ContactPage(self.driver)

    def add_member_fail(self):
        self.driver.find_element_by_id('username').send_keys("fail name")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("1225fail")
        self.driver.find_element_by_id('memberAdd_mail').send_keys("1225fail.name")
        self.driver.find_element_by_css_selector('.js_btn_save').click()

        return ContactPage(self.driver)
