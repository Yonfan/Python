# -*- coding: utf-8 -*-

import requests
from lxml import etree
import time
from PIL import Image
import pytesseract


class ZhihuSpider:

    def __init__(self):
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        self.loginUrl = 'https://www.zhihu.com/#signin'

    def parse_url(self, url):
        # 创建Session进行请求
        session = requests.session()
        response = session.get(url, headers=self.headers)
        return response.content.decode()

    def captcha(self, data):
        with open('captcha.jpg', 'wb') as f:
            f.write(data)
        time.sleep(3)
        image = Image.open('captcha.jpg')
        text = pytesseract.image_to_string(image)
        print("机器识别后的验证码为：", text)
        command = input("请输入Y表示同意使用，按其他键自行重新输入：")
        if (command == 'Y' or command == 'y'):
            return text
        else:
            return input("输入验证码：")

    def zhihulogin(self, username, password):
        # 获取页面信息
        html_str = self.parse_url(self.loginUrl)

        # 找到name属性值为_xsrf的input标签，取出value的值
        elements = etree.HTML(html_str)
        value = elements.xpath("//input[@name='_xsrf']/@value")
        if value:
            print("value:", value)
        else:
            # 特么的之前还有验证码为啥现在就没有啦？
            print("没有找到！！！")

        # 取出验证码
        captcha_url = 'https://www.zhihu.com/captcha.gif?r=%d&type=login' % (time.time() * 1000)
        response = requests.session().get(captcha_url, headers=self.headers)
        print(response.content)

        # 构造登录数据
        data = {
            "_xsrf": value,
            "email": username,
            "password": password,
            "remember_me": True,
            "captcha": self.captcha(response.content)
        }


if __name__ == '__main__':
    zhuhu = ZhihuSpider()
    zhuhu.zhihulogin('18872729852', 'YANGFAN0711')
