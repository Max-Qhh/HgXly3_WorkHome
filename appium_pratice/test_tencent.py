# -*- coding: utf-8 -*-
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestTenct():

    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.WwMainActivity",
            "noReset": "true",
            "skipDeviceInitialization": "true",
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true",
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('name, gender, phone', [
        ("app-user1", "男", "18600000001"),
        ("app-user2", "女", "18600000002"),
        ("app-user3", "男", "18600000003")
    ])
    def test_addmember(self, name, gender, phone):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("添加成员").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element_by_xpath("//*[@text='男']").click()
        self.driver.find_element_by_xpath(f"//*[@text='{gender}']").click()
        self.driver.find_element_by_id("com.tencent.wework:id/fuy").send_keys(phone)
        self.driver.find_element_by_id("com.tencent.wework:id/ie7").click()
        # mytoast = self.driver.find_element_by_xpath("//*[@text='添加成功']").text
        mytoast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        assert "添加成功" == mytoast

        # failtext = self.driver.find_element_by_xpath("//*[contains(@text,'手机已存在于通讯录')]")
        # assert failtext == "手机已存在于通讯录，无法添加"

    @pytest.mark.skip
    def test_daka(self):
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().'
                                 'text("打卡").instance(0));').click()
        self.driver.find_element_by_xpath("//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        r = self.driver.find_element_by_id("com.tencent.wework:id/pt").text
        assert "外出打卡成功" == r
