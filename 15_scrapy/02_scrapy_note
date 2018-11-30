## 使用scrapy的总结

### scrapy爬虫的几个主要步骤：
1. 新建scrapy爬虫项目：
`scrapy startproject 项目名`
2. 在爬虫目录下新建Demospider.py文件:
`scrapy genspider 爬虫名字 ‘爬取的域名’`
3. 明确爬虫的目标：（个人理解为爬虫取出来的数据名字）
在items.py里面写入所需数据的名字作为一个item，在后面取出数据的时候填充到item中
4. 存储内容（pipeline）：在pipeline中取出item中的数据并作一些处理：
    - 其中需要注意的是先要在setting.py文件中将ITEM_PIPELINE中打开
    - 处理的方式有很多种，但是一般分为3个步骤：
        1. `__init__`函数里面初始化将要写入的文件:
        `self.file = open('tencent.json', 'w', encoding='utf-8')`
        2. `process_item`函数处理item，一般将item序列化后写入
        3. `close_spider`函数将打开的IO文件关闭
        
 ### 一些小细节：
 - 当从命令行输入执行scrapy时候会发现命名行会将请求的数据什么的都显示在上面，一片混乱的，不太容易看清，这时候我们就需要用log文件，在setting.py文件添加：
 ```python
# 设置log日志
LOG_FILE = "TencentSpider.log"
LOG_LEVEL = "INFO"
```
- 当使用Crawlscrapy模板的时候
    - 不需像以前那种写法，构造下一页的url地址并加入Request队列中：
```python
# 发送新的url请求加入待爬队列，并调用回调函数 self.parse
yield scrapy.Request(url, callback=self.parse)
# 而是通过rule,使用正则表达式匹配提取的链接
rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )
```
**注意此时的callback函数千万不能写成parse，由于CrawlSpider使用parse方法来实现其逻辑，如果覆盖了parse方法，crawlspider将会运行失败！**   

- loggging的设置\
通过在setting.py中进行以下设置可以被用来配置logging:
    1. LOG_ENABLED 默认: True，启用logging
    2. LOG_ENCODING 默认: 'utf-8'，logging使用的编码
    3. LOG_FILE 默认: None，在当前目录里创建logging输出文件的文件名
    4. LOG_LEVEL 默认: 'DEBUG'，log的最低级别
    5. LOG_STDOUT 默认: False 如果为 True，进程所有的标准输出(及错误)将会被重定向到log中。例如，执行 print "hello" ，其将会在Scrapy log中显示。

