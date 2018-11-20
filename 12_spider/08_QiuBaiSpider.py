# -*- coding: utf-8 -*-
import requests
from lxml import etree
import json

class QiuBaiSpider:

    def __init__(self):
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}


    def get_url_list(self): # 构造url地址
        url_list = [self.url_temp.format(i) for i in range(1,14)]
        return  url_list

    def parse_url(self, url): # 请求url地址获取响应
        print("now parsing :", url)
        response = requests.get(url,headers=self.headers)
        return  response.content.decode()

    def get_content_list(self, html_str): # 提取页面数据
        content_list = []
        elements = etree.HTML(html_str)
        # 1. 分组
        div_list = elements.xpath("//div[@id='content-left']/div")
        for div in div_list:
            item = {}
            item["author_name"] = div.xpath(".//h2/text()")[0].strip()
            item["author_age"] = div.xpath(".//div[@class='author clearfix']/div/text()")
            item["author_age"] = item["author_age"][0] if len(item["author_age"])>0 else None
            item["content"] = div.xpath(".//div[@class='content']/span/text()")
            item["content"] = item["content"][0].strip() if len(item["content"])>0 else None
            item["stats_vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")
            item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"])>0 else None
            item["comments_nums"] =  div.xpath(".//span[@class='stats-comments']//i/text()")[0]
            item["img_url"] = div.xpath(".//div[@class='thumb']//img/@src")
            item["img_url"] = item["img_url"][0] if len(item["img_url"])>0 else None
            content_list.append(item)
        return  content_list

    def save_content_list(self, content_list):
        with open("QiuBai.txt","a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")
        print("保存成功！")


    def run(self): # 实现主要逻辑
        # 1.根据url地址的规律，构造url___list
        url_list = self.get_url_list()
        # 2.发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.提取数据
            content_list = self.get_content_list(html_str)
            # 4.保存数据
            self.save_content_list(content_list)

if __name__ == '__main__':
    qiubai = QiuBaiSpider()
    qiubai.run()

