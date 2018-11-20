# -*- coding: utf-8 -*-
import requests

# 实例化session
session = requests.session()

# 使用session发送post请求，获取对方保存在本地的cookie
post_url = "https://passport.zcool.com.cn/login_jsonp_active.do"

headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}


post_data = {
    "username": "***************",
    "password": "****************"
}

session.post(post_url, headers=headers, data=post_data)

# 在使用session 请求登录后的页面
url = "https://my.zcool.com.cn/focus/activity"

response = session.get(url, headers=headers)

with open("zcool4.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode())
