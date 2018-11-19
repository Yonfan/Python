# -*- coding: utf-8 -*-

import requests

url = "https://my.zcool.com.cn/focus/activity"
# 不使用cookie的时候会跳入登录页面
# headers = {
#     'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
# 使用了cookie登录后将会登陆进去


headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}


cookie = "_uab_collina=154254363120983227467882; gr_user_id=f191cfdd-14c9-47b0-a686-e1b0b5031727; UM_distinctid=164d45e33755f-0ee6314a8c2d19-b34356b-15f900-164d45e3376723; zid=1532571610hfgk; grwng_uid=257afad8-a278-446b-9663-f47b1fdf9459; 9f390e7b65f441ab_gr_last_sent_cs1=17655780; cn_e716846022b75pef3c0d_dplus=%7B%22distinct_id%22%3A%20%22164d45e33755f-0ee6314a8c2d19-b34356b-15f900-164d45e3376723%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201536137708%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201536137708%7D%7D; up_location_prompt=1; isnv=1; nav_tab_home=1; 9f390e7b65f441ab_gr_cs1=17655780; gr_cs1_8b3f287c-e3f8-4d8f-84b7-170229ee37a5=uid%3A0; gr_session_id_bd647439edc1d679=a1fbd100-01f2-4058-9c89-1ad956de3b1a; pplgdtk=TjFWNVdGblVtYjhOQ3Q5QUQ4d3lEdGRwSzdWbmw5bDFsT1M5KzJ0amR0WVJLR05Yb2FrTUpCZk9y%0AcU9JdGFVWlJGWEgrSFFlSE1qYVZEVWlzRXpjUWtIM2s1VFhvUnlCM2l0b1cySFkrWTJOUEg1Q1I0%0AM00wVUZLaXM3YUJpTXdFSEMxSU9DTm5MUHpRZjlibE41NlJjTENidzJ2ZkgvQU9tOHF6OUhuT2sr%0AMkhKUDRBOHZicmc9PT9hcHBJZD0xJmtleUlkPTE%3D; JSESSIONID=aaaE990ikhyFUcHwwPmCw; gr_session_id_acec0eb2dafeaf05=5db55145-fc28-49d7-bfda-60644f213beb; gr_cs1_5db55145-fc28-49d7-bfda-60644f213beb=uid%3A17655780; gr_session_id_acec0eb2dafeaf05_5db55145-fc28-49d7-bfda-60644f213beb=true; active=1; zui=%7B%22memberType%22:0,%22memberProfession%22:%22%E8%AE%BE%E8%AE%A1%E7%88%B1%E5%A5%BD%E8%80%85%22,%22memberGender%22:%22%E7%94%B7%22,%22pageUrl%22:%22https://www.zcool.com.cn/u/17655780%22,%22username%22:%22Z75936553%22,%22avatar%22:%22https://static.zcool.cn/git_z/z/images/boy.png%22,%22id%22:17655780%7D; zcool_logon_new=17655780%7C%7C%7Cnull%7C%7Cnull%7C20181118202116%7C271627C44675A94130559086A433ABE1; zcool_logon_hw=17655780%7CZ75936553%7Chttps%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F1noavatar.gif%7C18872729852%7C20181118202116%7C97C270F14F32BCBB6D9B9EB79CBDEA4F; activeDay=contentId%3D7592435_3%26day%3D2018-11-18"

cookie_dict = {i.split("=")[0]:i.split("=")[-1] for i in cookie.split("; ")}

print(cookie_dict)


response = requests.get(url, cookies=cookie_dict)

with open("zcool2.html","w",encoding="utf-8") as f:
    f.write(response.content.decode())