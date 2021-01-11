# -*- coding: utf-8 -*-
from appium import webdriver

from tencent_po.page.base_page import BasePage
from tencent_po.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver == None:
            caps = {
                "platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.WwMainActivity",
                # 不清空缓存启动app
                "noReset": "true",
                # 设置等待页面空闲状态的时间为0s
                # "settings[waitForIdleTimeout]": "0",
                # 跳过安装、权限设置等操作
                "skipDeviceInitialization": "true",
                "unicodeKeyBoard": "true",
                "resetKeyBoard": "true",
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(10)
        else:
            # 根据caps内设置的app信息启动app
            self.driver.launch_app()
        # 返回对象自身或返回归属类,简单的链式调用
        return self

    def stop(self):
        self.driver.quit()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    # -> 描述函数的返回类型
    def goto_main(self) -> MainPage:
        return MainPage(self.driver)
