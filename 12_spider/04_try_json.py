# -*- coding: utf-8 -*-
import requests
import json

url = "https://fanyi.baidu.com/basetrans"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) "
                  "Version/11.0 Mobile/15A372 Safari/604.1", "Referer": "https://fanyi.baidu.com/"}

query_str = input("请输入要翻译的内容：")

data = {"query": query_str,
        "from": "zh",
        "to": "en"}

response = requests.post(url, data, headers=headers)  # 发送post请求

html_str = response.content.decode() # 获取的是json字符串

str_dict = json.loads(html_str) # 将json字符串转换成字典

print(str_dict)

ret = str_dict["trans"][0]["dst"]

print("翻译结果是：",ret)






