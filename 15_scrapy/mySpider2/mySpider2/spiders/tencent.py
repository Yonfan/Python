# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from mySpider2.items import TencentItem

class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    # link_extractor：是一个Link Extractor对象，用于定义需要提取的链接。
    # 其实跟上面的正则表达式类似
    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for each in response.xpath('//*[@class="even"]'):
            item = TencentItem()

            name = each.xpath('./td[1]/a/text()').extract()
            name = name[0] if len(name) > 0 else None
            detailLink = each.xpath('./td[1]/a/@href').extract()
            detailLink = detailLink[0] if len(detailLink) > 0 else None
            positionInfo = each.xpath('./td[2]/text()').extract()
            positionInfo = positionInfo[0] if len(positionInfo) > 0 else None
            peopleNumber = each.xpath('./td[3]/text()').extract()
            peopleNumber = peopleNumber[0] if len(peopleNumber) > 0 else None
            workLocation = each.xpath('./td[4]/text()').extract()
            workLocation = workLocation[0] if len(workLocation) > 0 else None
            publishTime = each.xpath('./td[5]/text()').extract()
            publishTime = publishTime[0] if len(publishTime) > 0 else None

            item['name'] = name
            item['detailLink'] = detailLink
            item['positionInfo'] = positionInfo
            item['peopleNumber'] = peopleNumber
            item['workLocation'] = workLocation
            item['publishTime'] = publishTime

            print("*" * 100)
            print(item)
            print("*" * 100)

            yield item
