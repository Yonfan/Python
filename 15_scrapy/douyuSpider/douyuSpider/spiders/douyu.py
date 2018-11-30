# -*- coding: utf-8 -*-
import scrapy
import json
from douyuSpider.items import DouyuspiderItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['m.douyu.com']

    page = 1
    url = 'https://m.douyu.com/api/room/list?page={}&type=yz'
    start_urls = [url.format(page)]

    def parse(self, response):
        # 返回从json里面获取data段数据集合
        data = json.loads(response.text)["data"]["list"]

        for each in data:
            item = DouyuspiderItem()

            item["nickname"] = each["nickname"]
            item["roomName"] = each["roomName"]
            item["roomSrc"] = each["roomSrc"]
            item["hn"] = each["hn"]

            yield item

        self.page += 1
        print("*" * 100)
        print(self.url.format(self.page))
        print("*" * 100)
        yield scrapy.Request(self.url.format(self.page), callback=self.parse)
