# -*- coding: utf-8 -*-
import requests


# 一、在不使用session和cookie字段的时候我们这样请求是会跳入登录页面的的
# url = "http://my.sina.com.cn/"
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
# response = requests.get(url,headers=headers)
# with open("Sina.html", "w", encoding="utf-8") as f:
#     f.write(response.content.decode())
# 此时我们看到的是登录页面而不是个人主页！



# 二、现在我们开始使用cookie字段放入headers中进行登录：
# headers2 = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
#            "Cookie": "SINAGLOBAL=172.16.118.85_1532508346.504717; SCF=Am7953Jhi8Uf9noYWipubbN4f-SMqJya6p3mLlK_rF8Xin7k6xW17nK0hQpDwg4NJKAAU_rvnrICwBh4ZJYhSWM.; UOR=www.baidu.com,news.sina.com.cn,; U_TRS1=00000046.19a62bf.5b64fd53.d8dc1d3f; SGUID=1541497777195_22429079; lxlrttp=1541383354; ULV=1541499015491:6:2:2:10.13.240.92_1541497774.656198:1541497774112; Apache=172.16.118.85_1542703003.158886; U_TRS2=00000031.518737dd.5bf3c8b8.c37d927c; bdshare_firstime=1542703290662; WEB2=57dab1382fe02d4d7ed4ecd269b8ac6b; ULOGIN_IMG=tc-6f220f496cc189cf3ed689d397446634c7bf; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFjK_N7V9F8Jjm9-EBwLqr05NHD95Qfe0B01K5cehzEWs4Dqcj-i--ci-2fiKyWi--NiKnfi-24PfYt; ALF=1574301145; sso_info=v02m6alo5qztKWRk5ilkJOUpY6EhKWRk5yljoOUpZCTpZ-Xspm1mpaQvY2TjLSMs6SwjaOAsoygwMA=; SUB=_2A2528MoKDeRhGeNN71EY8CjMyT6IHXVVh7zCrDV_PUJbm9AKLXbjkW9NSaegVShmJla8bcu1onu0pci8UA8jxHW-"}
# response = requests.get(url,headers=headers2)
# with open("Sina.html", "w", encoding="utf-8") as f:
#     f.write(response.content.decode())
# 此时观察sina.html这个页面是登陆后的页面了





# 三、使用Session获取cookie登录
# 实例化session
session = requests.session()

# 使用session发送post请求，获取对方保存在本地的cookie
post_url = "https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}


post_data = {
    "username":"此处放你的账号",
    "password":"此处放入你的密码"
}

session.post(post_url,data=post_data,headers=headers)


# 在使用session 请求登录后的页面
url = "http://my.sina.com.cn/"

response = session.get(url, headers=headers)
print(response)
with open("Sina.html", "w", encoding="utf-8") as f:
    f.write(response.content.decode())
