# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    nickname = scrapy.Field()       # 主播的名字
    roomName = scrapy.Field()       # 房间名字
    roomSrc = scrapy.Field()        # 照片的url路径
    imagesPath = scrapy.Field()    # 照片的物理路径
    hn = scrapy.Field()             # 人数
