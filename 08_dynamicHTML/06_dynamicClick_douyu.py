# -*- coding: utf-8 -*-

# python 测试模块
from selenium import webdriver
import unittest
from lxml import etree


class douyuSelenium(unittest.TestCase):

    # 初始化的方法
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.url = 'http://www.douyu.com/directory/all'

    def get_new_show(self, elements):
        new_show = []
        li_new = elements.xpath("//div[@class='items items01 new-show-live clearfix']/ul/li")
        for li in li_new:
            item = {}
            item["title"] = li.xpath(".//h3/text()")
            item["author"] = li.xpath(".//p/span/text()")
            item["classfiy"] = li.xpath(".//span[@class='tag ellipsis']/text()")
            new_show.append(item)
        return new_show

    def get_main_show(self, elements):
        main_show = []
        li_main = elements.xpath("//ul[@id='live-list-contentbox']/li")
        for li in li_main:
            item = {}
            item["title"] = li.xpath(".//h3/text()")[0].strip()
            item["author"] = li.xpath(".//span[@class='dy-name ellipsis fl']/text()")[0]
            item["nums"] = li.xpath(".//span[@class='dy-num fr']/text()")[0]
            item["classfiy"] = li.xpath(".//span[@class='tag ellipsis']/text()")[0]
            main_show.append(item)
        return main_show

    def save_content(self, main_show):
        for show in main_show:
            with open('douyuTV.txt', 'a', encoding='utf-8') as f:
                str = "房间标题：" + show["title"] + "\t分类：" + show["classfiy"] + "\t主播名字：" + show["author"] + "\t人气：" + \
                      show["nums"]
                f.write(str)
                f.write('\n')
        print("保存成功！")

    # 具体的测试用例方法，一定要用test开头
    def testDouyu(self):
        # 请求
        self.driver.get(self.url)
        first = 1
        while True:
            # 获取请求的内容
            html_str = self.driver.page_source
            elements = etree.HTML(html_str)

            # 分组 先爬取新秀 爬取其他的栏目
            # 1、爬取新秀
            if first == 1:
                new_show = self.get_new_show(elements)
            # 2、主要栏目
            main_show = self.get_main_show(elements)

            # 3、保存
            self.save_content(main_show)

            first = 0

            # 指定元素找到则返回 非 -1 ，表示达到最后一页， 退出循环
            if self.driver.page_source.find('shark-pager-disable-next') != -1:
                break

            # 模拟点击下一页
            self.driver.find_element_by_class_name('shark-pager-next').click()


# 退出时候清理方法
def tearDown(self):
    print('加载完成...')
    self.driver.quit()


if __name__ == '__main__':
    unittest.main()
