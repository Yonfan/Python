# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
        # 保存返回的页面信息
        # with open('teachers.html', 'w', encoding='utf-8') as f:
        #     f.write(response.text)

        # 存放老师信息的集合
        # items = []

        # 分组：
        div_list = response.xpath("//div[@class='li_txt']")

        # 提取数据：
        for each in div_list:
            # 将我们得到的数据封装到一个itcastItem对象
            item = ItcastItem()

            # extract()方法返回的都是unicode字符串
            name = each.xpath(".//h3/text()").extract()
            title = each.xpath(".//h4/text()").extract()
            info = each.xpath(".//p/text()").extract()

            # xpath返回的是包含一个元素的列表
            item["name"] = name[0]
            item["title"] = title[0]
            item["info"] = info[0]

            # items.append(item)

            # 将获取的数据交给pipelines
            yield item

        # 直接返回最后数据，暂时不做管道处理
        # return items
