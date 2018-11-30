# -*- coding: utf-8 -*-

from selenium import webdriver
import time

url = 'https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action='

driver = webdriver.PhantomJS()
driver.get(url)

# 往下滚动10000像素
js = 'document.body.scrollTop=10000'
time.sleep(3)

# 查看页面快照
driver.save_screenshot('douban.png')

# 执行js语句
driver.execute_script(js)
time.sleep(10)

# 查看页面快照
driver.save_screenshot('newdouban.png')

driver.quit()

