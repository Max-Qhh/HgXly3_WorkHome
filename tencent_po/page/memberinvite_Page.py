# -*- coding: utf-8 -*-

# 点击手动添加界面
from appium.webdriver.common.mobileby import MobileBy

from tencent_po.page.base_page import BasePage
from tencent_po.page.conatctedit_page import ConatctEditPage


class MemberInvitePage(BasePage):
    addmember_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    def addconect_menual(self):
        # 点击 手动输入添加
        self.find_and_click(self.addmember_element)
        return ConatctEditPage(self.driver)

    def get_toast(self):
        toast_element = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        mytoast = self.find_and_get_text(toast_element)
        return mytoast
