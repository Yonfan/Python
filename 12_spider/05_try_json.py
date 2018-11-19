# -*- coding: utf-8 -*-
import requests
import json

url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?os=ios&for_mobile=1&start=0&count=18&loc_id=108288&_=1542610877052"

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) "
                  "Version/11.0 Mobile/15A372 Safari/604.1",
    "Referer": "https://m.douban.com/tv/american"}


response = requests.get(url, headers=headers)

html_str = response.content.decode()

json_str = json.loads(html_str)

# print(json_str)

with open("dianying.txt","w",encoding="utf-8") as f:
    f.write(json.dumps(json_str,ensure_ascii=False,indent=2))

# ensure_ascii=False, 让中文显示成中文
# indent=2 让下一行在上一行的基础上空格 表示空2格


# print(html_str)
