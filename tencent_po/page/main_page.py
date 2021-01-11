# -*- coding: utf-8 -*-

# 首页界面-点击通讯录
from appium.webdriver.common.mobileby import MobileBy

from tencent_po.page.addresslist_page import AddressListPage
from tencent_po.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    addresslist_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def click_addresslist(self):
        # 点击通讯录
        self.find(self.addresslist_element).click()
        return AddressListPage(self.driver)
