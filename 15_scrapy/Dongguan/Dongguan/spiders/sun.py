# -*- coding: utf-8 -*-//div[@class='greyframe']/table[2]//td/a[@class='news14']/@href
import scrapy
from Dongguan.items import DongguanItem


class SunSpider(scrapy.Spider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']

    page = 0  # 30个为一页
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page={}'
    start_urls = [url.format(page)]

    def parse(self, response):
        # 去取出每个帖子里面的链接列表
        links = response.xpath("//div[@class='greyframe']/table[2]//td/a[@class='news14']/@href").extract()

        # 迭代发送每个帖子的请求，调用parse_item方法处理
        for link in links:
            yield scrapy.Request(link, callback=self.parse_item)

        # 设置终止的页码条件，并且每次发送的新的页面请求调用parse方法处理
        if self.page <= 71130:
            self.page += 30
            yield scrapy.Request(self.url.format(self.page), callback=self.parse)

    # 处理每个帖子
    def parse_item(self, response):
        # 实例化一个item对象
        item = DongguanItem()

        # 取出数据
        # 标题
        item["title"] = response.xpath("//div[contains(@class, 'pagecenter p3')]//strong/text()").extract()[0]
        # 编号
        item["number"] = item["title"].split("  ")[-1].split(":")[-1].strip()
        # 文字内容:1.带有图片的文字内容 2、不带图片的纯文字内容
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        # 如果没有内容，则取出没有图片情况下的文字内容列表
        if len(content) == 0:
            content = response.xpath("//div[@class='c1 text14_2']/text()").extract()
            # content为列表，通过join方法拼接为字符串，并去除首尾空格
            item['content'] = "".join(content).strip()
        else:
            item['content'] = "".join(content).strip()

        # 链接
        item["url"] = response.url

        yield item
