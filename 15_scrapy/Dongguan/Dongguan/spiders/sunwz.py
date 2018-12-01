# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Dongguan.items import DongguanItem

'''
记录遇到的一个问题：
当使用Rule在爬取这个网站的时候会发现：
使用Rule规则的时候，发现提取出来的链接只有6条，而不是所有的
如：
[Link(url='http://wz.sun0769.com/index.php/question/questionType?type=4', text='[投诉]', fragment='', nofollow=False),
 Link(url='http://wz.sun0769.com/index.php/question/questionType?type=4&page=30', text='2', fragment='', nofollow=False),
 Link(url='http://wz.sun0769.com/index.php/question/questionType?type=4&page=60', text='3', fragment='', nofollow=False),
 Link(url='http://wz.sun0769.com/index.php/question/questionType?type=4&page=90', text='4', fragment='', nofollow=False),
 Link(url='http://wz.sun0769.com/index.php/question/questionType?type=4&page=120', text='5', fragment='', nofollow=False),
 Link(url='http://wz.sun0769.com/index.php/question/questionType?type=4&page=100530', text='>>', fragment='', nofollow=False)]
 
 当爬取的时候就只爬取了这六条链接里面的内容
'''

class SunwzSpider(CrawlSpider):
    name = 'sunwz'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    # 每一页的配置规则
    pageLink = LinkExtractor(allow=r'type=4')
    # 每个帖子的匹配规则
    contentLink = LinkExtractor(allow=r'/html/question/\d+/\d+.shtml')

    rules = (
        # 本案例为特殊情况，需要调用deal_links方法处理每个页面里的链接
        Rule(pageLink, process_links='deal_links', follow=True),
        Rule(contentLink, callback='parse_item')
    )

    # 需要重新处理每个页面里的链接，将链接里的‘Type&type=4?page=xxx’替换为‘Type?type=4&page=xxx’（或者是Type&page=xxx?type=4’替换为‘Type?page=xxx&type=4’），否则无法发送这个链接
    def deal_links(self, links):
        for link in links:
            print(link.url)
            print("*" * 100)
            link.url = link.url.replace("?", "&").replace("Type&", "Tpye?")
            print(link.url)
        return links

    def parse_item(self, response):
        # 观察url是否出现变化
        print(response.url)

        item = DongguanItem()
        # 标题
        item['title'] = response.xpath('//div[contains(@class, "pagecenter p3")]//strong/text()').extract()[0]

        # 编号
        item["number"] = item["title"].split("  ")[-1].split(":")[-1].strip()

        # 文字内容，默认先取出有图片情况下的文字内容列表
        content = response.xpath('//div[@class="contentext"]/text()').extract()
        # 如果没有内容，则取出没有图片情况下的文字内容列表
        if len(content) == 0:
            content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            # content为列表，通过join方法拼接为字符串，并去除首尾空格
            item['content'] = "".join(content).strip()
        else:
            item['content'] = "".join(content).strip()

        # 链接
        item['url'] = response.url

        yield item



