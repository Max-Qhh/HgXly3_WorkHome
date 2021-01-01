# -*- coding: utf-8 -*-
import time

import yaml
from selenium import webdriver

# 复用浏览器的方法获取cookie序列化保存到yaml(当前窗口复用)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_get_cookie():
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(10)

    vx_cookies = driver.get_cookies()
    with open("D:/PycharmProjects/HogWartsXly3/selenium_pratice_adduser/cookie.yaml", "w", encoding="utf-8") as f:
        yaml.dump(vx_cookies, f)


def test_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()

    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    with open("D:/PycharmProjects/HogWartsXly3/selenium_pratice_adduser/cookie.yaml")as f:
        vx_login_cookie = yaml.safe_load(f)
    for cookie in vx_login_cookie:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")

    # driver.find_element_by_id("menu_contacts").click()
    # driver.find_element_by_link_text("添加成员").click()
    # driver.find_element_by_id("username").send_keys("成员A")
    # driver.find_element_by_id("memberAdd_acctid").send_keys("2020122201")
    # driver.find_element_by_id("memberAdd_mail").send_keys("966322144@163.com")
    # time.sleep(3)
    #
    # driver.find_element_by_link_text("保存并继续添加").click()
    # # driver.find_element_by_xpath("//*[@id='js_contacts61']/div/div[2]/div/div[4]/div/form/div[3]/a[1]").click()
    # time.sleep(3)
    #
    # driver.find_element_by_id("username").send_keys("成员B")
    # driver.find_element_by_id("memberAdd_acctid").send_keys("2020122202")
    # driver.find_element_by_id("memberAdd_mail").send_keys("258793@qq.com")
    # time.sleep(3)
    # driver.find_element_by_link_text("保存").click()
    # time.sleep(3)

    # #
    driver.find_element_by_id("menu_contacts").click()
    ele = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")

    # 显式等待，等待元素是可点击状态
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(ele))
    # 解决点击无效问题；设置死循环多次点击，直到目标元素出现后，跳出死循环
    while True:
        # *是解数组
        driver.find_element(*ele).click()
        element = driver.find_elements_by_id('username')
        if len(element) > 0:
            break
    driver.find_element_by_id('username').send_keys("成员C")
    driver.find_element_by_id("memberAdd_acctid").send_keys("1222CYC")
    driver.find_element_by_id('memberAdd_mail').send_keys("chengyuan@sina.com")
    driver.find_element_by_css_selector('.js_btn_save').click()
    time.sleep(3)

    eles = driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(2)")
    name_list = []
    for value in eles:
        # 获取元素属性title的值，存入list内
        print(value.get_attribute("title"))
        name_list.append(value.get_attribute("title"))
    # 断言目标名字是否在列表内
    assert "成员C" in name_list
    print(name_list)