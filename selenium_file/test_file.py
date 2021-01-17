# -*- coding: utf-8 -*-
from time import sleep

from selenium_file.Base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_xpath("//*[@id='form']/span[1]/span[1]").click()
        # 可以通过send.keys可以上传文件，识别上传，添加图片地址
        self.driver.find_element_by_xpath("//*[@id='form']/div/div[2]/div[2]/input").send_keys(
            "C:/Users/Administrator/Pictures/压缩版panda.png")
        sleep(3)