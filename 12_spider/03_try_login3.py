# -*- coding: utf-8 -*-
import requests

# 实例化session
session = requests.session()

# 使用session发送post请求，获取对方保存在本地的cookie
post_url = "https://passport.zcool.com.cn/login_jsonp_active.do"

headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}

datastr = {
    "jsonpCallback": "jQuery19104615771324313176_1542545164725",
    "appId": "1006",
    "username": "18872729852",
    "password": "08cba4c74028157bb51c3f33b7d77a59a951578c4b7cf4cceb02dc5e86c834a2",
    "autoLogin": "0",
    "code": "",
    "service": "https://www.zcool.com.cn/u/17655780",
    "appLogin": "https://www.zcool.com.cn/login_cb",
    "_": "1542545164727"}

post_data = {
    "username": "18872729852",
    "password": "YANGFAN0711"
}

session.post(post_url, headers=headers, data=post_data)

# 在使用session 请求登录后的页面
url = "https://my.zcool.com.cn/focus/activity"

response = session.get(url, headers=headers)

with open("zcool4.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode())
