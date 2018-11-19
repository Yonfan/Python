# -*- coding: utf-8 -*-
import requests

url = "https://fanyi.baidu.com/basetrans"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) "
                  "Version/11.0 Mobile/15A372 Safari/604.1", "Referer": "https://fanyi.baidu.com/"}

data = {"query": "我爱你",
        "from": "zh",
        "to": "en"}

response = requests.post(url, data, headers=headers)  # 发送post请求
print("*"*100)
print("response.url", response.url)  # 我们需要的不是一个返回的状态码而是获取响应的字符串
print("-"*100)
print("response.request.url", response.request.url)
print("*"*100)
print("response.request.headers", response.request.headers)
print("-"*100)
print("response.headers", response.headers)
print("*"*100)
print(response.content.decode())
# 为什么会出现没有内容？
# 有二种可能：
# 1、没有 请求成功
# 2、对方服务器识别我们为爬虫程序拒绝响应内容
# 此时我们就需要丰富我们的headers作为一种伪装去请求（伪装自己是浏览器请求而不是爬虫）
