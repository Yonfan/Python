# -*- coding: utf-8 -*-

'''
Selenium 库里有个叫 WebDriver 的 API。WebDriver 有点儿像可以加载网站的浏览器，但是它也可以像 BeautifulSoup 或者其他 Selector 对象一样用来查找页面元素，与页面上的元素进行交互 (发送文本、点击等)，以及执行其他动作来运行网络爬虫。
'''

# 导入webdriver
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS()

# get方法会一直等到页面加载完才会继续执行程序，通常测试会在这里选择 time.sleep(2)
driver.get("http://www.baidu.com")

# 获取页面名叫 wrapper 的id标签的文本内容
data = driver.find_element_by_id('wrapper').text

# 打印
# print(data)

# 打印页面标题
print(driver.title)

# 生成当前页面快照并保存
# driver.save_screenshot('baidushot.png')

# id='kw'是百度的搜索框，输入字符‘长城’
driver.find_element_by_id('kw').send_keys(u'长城')

# id='su'是百度的搜索按钮，click是模拟点击事件
driver.find_element_by_id('su').click()

# 莫里奥：在这里停顿！2秒。不停顿在这里会报错
time.sleep(2)

# 为啥要点击二次？因为点击第一次没有数据只是在输入框中键入了文字
driver.find_element_by_id('su').click()

# 获取新的页面快照
# driver.save_screenshot('长城.png')

# 打印网页渲染后的代码
# print(driver.page_source)

# 打印不好看，直接输出为html文件吧
# with open('baidu.html', 'w', encoding='utf-8') as f:
#     f.write(driver.page_source)

# 获取页面的cookie 那么下列二者有什么区别呢？
# print(driver.get_cookies())

# 调用键盘按键操作时需要引入的keys包

# ctrl+a 全选输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')

# ctrl+x 剪切输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

# 输入框重新输入内容
driver.find_element_by_id('kw').send_keys('痛仰乐队')

# 模拟Enter回车键
driver.find_element_by_id('su').send_keys(Keys.ENTER)
time.sleep(2)  # 没有这个就会报错！
driver.find_element_by_id('su').click()

# 清除输入框内容
# driver.find_element_by_id("kw").clear()

# 生成新的页面快照
driver.save_screenshot("itcast.png")

# 获取当前的url
print(driver.current_url)

# 关闭当前页面，如果只有一个页面将会关闭浏览器
driver.close()

# 关闭浏览器
driver.quit()
