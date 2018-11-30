# -*- coding: utf-8 -*-

import requests
import re


class NeihanSpider:

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def parse_url(self, url):
        print("当前url为：", url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode('gbk')

    def get_content(self, html_str):
        pattern1 = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)
        content_list = pattern1.findall(html_str)  # 返回匹配成功的整个子串
        for content in content_list:
            print(content)
        pattern2 = re.compile(r'<span.*?class="pageinfo">.*?<strong>(\d+)</strong>', re.S)
        total = pattern2.findall(html_str)
        return content_list, int(total[0])

    def save_content(self, content_list, index):
        i = 1
        for content in content_list:
            with open('neihan.txt', 'a', encoding='utf-8') as f:
                data = "第{0}页第{1}条数据：".format(index, i)+content.strip()
                f.write(data)
                f.write('\n')
            i += 1
        print('保存成功！')

    def run(self):  # 主要逻辑
        index = 1
        while 1:
            # 1. 获取初始的url地址
            url = "http://www.neihan8.com/article/list_5_{}.html"
            # 2. 发送请求, 得到响应
            html_str = self.parse_url(url.format(index))
            # 3. 用正则表达式，获取数据
            content_list, total = self.get_content(html_str)
            # 4. 保存
            self.save_content(content_list, index)
            # 5. 构造下一页url地址
            index += 1
            if index > total:
                print('爬虫结束！总共%s页' % total)
                break


if __name__ == '__main__':
    neihan = NeihanSpider()
    neihan.run()
