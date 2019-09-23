# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class DoubanspiderPipeline(object):

    def __init__(self):
        self.file = open('douban.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        data = json.dumps(dict(item), ensure_ascii=False, indent=2)
        self.file.write(data + "\n")
        return item

    def close_spider(self, spider):
        self.file.close()