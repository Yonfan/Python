# -*- coding: utf-8 -*-
import requests

url = "https://www.baidu.com"

response = requests.get(url)    # 发送get请求
#print(response)                #返回的是一个状态码

# 获取网页的html的字符串
# response.encoding = 'utf-8'
# print(response.text)

# 获取网页的二进制编码格式
# print(response.content)

# 将上述响应的字节流转换成str类型
print(response.content.decode())

