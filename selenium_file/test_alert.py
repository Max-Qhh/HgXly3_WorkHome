# -*- coding: utf-8 -*-
import time

from selenium.webdriver import ActionChains

from selenium_file.Base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切换iframe
        self.driver.switch_to_frame("iframeResult")

        # 定义开始和结束的元素
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")

        # 使用ActionChains模块
        action = ActionChains(self.driver)
        # 调用拖拽方法（从元素一拖拽到元素二）(perform执行)
        action.drag_and_drop(drag, drop).perform()

        time.sleep(2)
        # 切换到alert下面并点击确认
        print("点击 alert 确认")
        self.driver.switch_to.alert.accept()

        # 点击运行（需要先切换到默认frame节点/父几点）
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id("submitBTN").click()
        time.sleep(3)
