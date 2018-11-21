# -*- coding: utf-8 -*-
import requests
import json

class SinaSpider:

    def __init__(self):
        self.url = "http://cre.mix.sina.com.cn/api/v3/get?sns_len=12&sns_offset=0&sns_pos=5&cre=mysinapc&mod=f&statics=1&merge=3&fields=url,reason&feed_fmt=1&rfunc=101&dedup=4&cateid=sina_all&offset={}&length=30&lid=-3000&_=1542766404871"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}

    def get_Url_list(self):
        url_list = [self.url.format(i*30) for i in range(0,30)]
        return url_list

    def parse_url(self,url):
        print("当前url为：",url)
        response = requests.get(url,self.headers)
        return response.content.decode()

    def get_content_list(self,content):
        dict_data = json.loads(content)
        result = dict_data["result"]
        total = result["total"]
        data = result["data"]
        print("新闻总数：", total)
        return data,total

    def save_content(self,data,index):
        with open("SinaNews.txt","a",encoding="utf-8") as f:
            f.write(json.dumps(data,ensure_ascii=False))
            f.write("\n")
        print("保存成功！当前第%d条" % index)

    def run(self): # 实现主要逻辑
        # 1.构造url_list
        url_list = self.get_Url_list()
        index = 0
        # 2.发送请求
        for url in url_list:
            content = self.parse_url(url)
            # 3.提取数据
            data,total = self.get_content_list(content)
            for singleNews in data:
                # 4.保存
                index += 1
                self.save_content(singleNews,index)
            if index>total: # 如果达到了总条数就退出
                print("爬取结束！")
                break

# 这样子写有问题：
#     1.没有结束标志
#     2.保存的内容一条data里面包含30条新闻，我们需要将30跳新闻分开！



if __name__ == '__main__':
    sinaspider = SinaSpider()
    sinaspider.run()