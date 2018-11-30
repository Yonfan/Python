# -*- coding: utf-8 -*-

'''
隐藏百度图片
'''

from selenium import webdriver

url = 'https://www.baidu.com'

driver = webdriver.PhantomJS()
driver.get(url)

# 给搜索输入框标红的js脚本
js = "var q=document.getElementById(\"kw\");q.style.border=\"2px solid red\";"

# 调用给搜索输入框标红的脚本
driver.execute_script(js)

# 查看页面快照
# driver.save_screenshot("redbaidu.png")


# js隐藏元素 将获取的图片元素隐藏
img = driver.find_element_by_xpath("//div[@id='lg']/img")
driver.execute_script("$(arguments[0]).hide()", img)

driver.save_screenshot("redbaidu.png")


# 向下滚动到页面底部
driver.execute_script("$('.scroll_top').click(function(){$('html,body').animate({scrollTop: '0px'}, 800);});")

#查看页面快照
driver.save_screenshot("nullbaidu.png")

driver.quit()
