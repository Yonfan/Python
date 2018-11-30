# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import TencentItem
import re


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):
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

            # 正则表达式寻找页码并换成下一页
            curpage = re.search('(\d+)', response.url).group(1)
            page = int(curpage) + 10
            url = re.sub('\d+', str(page), response.url)

            # 发送新的url请求加入待爬队列，并调用回调函数 self.parse
            yield scrapy.Request(url, callback=self.parse)

            # 将获取的数据交给pipeline
            yield item
