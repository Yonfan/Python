# -*- coding: utf-8 -*-
import scrapy
from DoubanSpider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = 'Douban'
    allowed_domains = ['movie.douban.com']
    start = 0
    url = "https://movie.douban.com/top250?start={}&filter="
    start_urls = [url.format(start)]

    def parse(self, response):
        # 创建豆瓣item
        item = DoubanspiderItem()

        movies = response.xpath("//div[@class='info']")

        for each in movies:
            title = each.xpath(".//span[@class='title']/text()").extract()[0]
            score = each.xpath(".//span[@class='rating_num']/text()").extract()[0]
            content = each.xpath("./div[@class='bd']/p[1]/text()").extract()
            info = each.xpath(".//span[@class='inq']/text()").extract()

            item['title'] = title if len(title) > 0 else None
            item['content'] = ";".join(content).replace(r"\n", "").strip()
            item['score'] = score
            item['info'] = info[0] if len(info) > 0 else None

            # 提交item
            yield item

        if self.start < 250:
            self.start += 25
            yield scrapy.Request(self.url.format(self.start), callback=self.parse)
