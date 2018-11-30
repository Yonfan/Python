# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.PhantomJS()
driver.get("http://221.233.24.23/eams/login.action")

# 输入账号密码
driver.find_element_by_name("username").send_keys("201871335")
driver.find_element_by_name("password").send_keys("110015")

# 模拟点击登录
driver.find_element_by_xpath("//input[@name='submitBtn']").click()

# 等待3秒
time.sleep(3)

# 生成登陆后快照
driver.save_screenshot("ytedu.png")

# 保存源码
with open("ytedu.html", "w", encoding='utf-8') as file:
    file.write(driver.page_source)

driver.quit()
