# -*- coding: utf-8 -*-

# 首页
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_pratice_adduser.page.add_member_page import AddMemberPage
from selenium_pratice_adduser.page.basepage import BasePage
from selenium_pratice_adduser.page.contact_page import ContactPage


# 继承BasePage的driver
class MainPage(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/loginpage_wx"

    # 去通讯录界面
    def goto_contact_page(self):
        # self.driver.find_element_by_id("menu_contacts").click()
        self.find(By.ID, "menu_contacts").click()

        # 面向对象，跳转到通讯录界面
        return ContactPage(self.driver)

    def goto_add_member_page(self):
        from selenium_pratice_adduser.page.add_member_page import AddMemberPage
        ele_main_add = (By.CSS_SELECTOR, ".index_service_cnt_item_title")
        self.wait_for_click(ele_main_add, 10)
        while True:
            self.find(By.CSS_SELECTOR, ".index_service_cnt_item_title").click()
            element = self.finds(By.ID, "username")
            if len(element) > 0:
                break
        return AddMemberPage(self.driver)
