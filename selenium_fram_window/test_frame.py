# -*- coding: utf-8 -*-

from selenium_fram_window.Base import Base

class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 进行frame切换（两种方式）
        self.driver.switch_to.frame("iframeResult")
        # self.driver.switch_to_frame("iframeResult")

        print(self.driver.find_element_by_id("draggable").text)

        # 切回parent_frame节点（两种方式）
        # self.driver.switch_to.parent_frame()
        # 切换回默认的frame，刚打开地址的frame节点
        self.driver.switch_to.default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
