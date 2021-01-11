# -*- coding: utf-8 -*-

# 编辑联系人界面（姓名，性别，手机号， 邮箱）
from appium.webdriver.common.mobileby import MobileBy
from tencent_po.page.base_page import BasePage



class ConatctEditPage(BasePage):

    def edit_name(self, name):
        name_element = (MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText")
        self.find(name_element).send_keys(name)
        return self

    def edit_genter(self, gender):
        gender_ele = (MobileBy.XPATH, "//*[@text='男']")
        self.find_and_click(gender_ele)
        # if gender == '男':
        #     self.wait_for_click((MobileBy.XPATH, "//*[@text='男']"))
        # else:
        #     self.wait_for_click((MobileBy.XPATH, "//*[@text='女']"))
        # return self
        self.wait_for_click((MobileBy.XPATH, f"//*[@text='{gender}']"))
        return self

    def edit_phonenm(self, phonenm):
        phone_ele = (MobileBy.ID, "com.tencent.wework:id/fuy")
        self.find(phone_ele).send_keys(phonenm)
        return self

    def edit_email(self, email):
        name_element = (MobileBy.XPATH, "//*[contains(@text,'邮箱')]/../android.widget.EditText")
        self.find(name_element).send_keys(email)
        return self

    def edit_save(self):
        from tencent_po.page.memberinvite_Page import MemberInvitePage
        self.find((MobileBy.ID, "com.tencent.wework:id/ie7")).click()
        return MemberInvitePage(self.driver)
