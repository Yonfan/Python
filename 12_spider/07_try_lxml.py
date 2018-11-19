# -*- coding: utf-8 -*-
import requests
from lxml import etree

url = "https://movie.douban.com/chart"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

response = requests.get(url, headers=headers)

html_str = response.content.decode()    # get the String of this HTML page

# print(html_str)

# 用lxml获取这个页面中的内容
elements = etree.HTML(html_str)


# 1.要求取得所有电影的url地址
href_list = elements.xpath("//div[@class='indent']/div/table//div[@class='pl2']/a/@href")
# print(href_list)

# 2.要求获取所有电影的名字
mvname_list = elements.xpath("//div[@class='indent']/div/table//a[@class='nbg']/@title")
# print(mvname_list)

# 3.要求获取所有电影的图片地址
mvnbg_list = elements.xpath("//div[@class='indent']/div/table//a[@class='nbg']/img/@src")
# print(mvnbg_list)

# 4.要求把每一个电影组成一个字典，字典中是电影的重要数据
#     思路：
#         1. 获取每一组
mv_group = elements.xpath("//div[@class='indent']/div/table")
# print(mv_group)
#         2. 根据每一组来获取每一项
for group in mv_group:
    item = {}
    # 获取电影名字
    item["title"] = group.xpath(".//div[@class='pl2']/a/text()")[0].replace("/","").strip()
    # print(item["title"])
    # 获取电影的url地址
    item["href"] = group.xpath(".//div[@class='pl2']/a/@href")
    # 获取电影的评分
    item["rating_nums"] = group.xpath(".//div[@class='pl2']/div/span[@class='rating_nums']/text()")
    # 获取电影的评价人数
    item["comment_nums"] = group.xpath(".//div[@class='pl2']/div/span[@class='pl']/text()")
    # 打印看看吧
    print(item)




