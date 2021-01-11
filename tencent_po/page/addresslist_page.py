# -*- coding: utf-8 -*-
from tencent_po.page.base_page import BasePage
from tencent_po.page.memberinvite_Page import MemberInvitePage

# 通讯录界面
class AddressListPage(BasePage):


    def add_member(self):
        self.find_by_croll_and_click("添加成员")
        return MemberInvitePage(self.driver)
