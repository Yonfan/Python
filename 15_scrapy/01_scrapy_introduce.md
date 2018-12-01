## 制作scrapy爬虫只需四步
- 新建项目(scrapy startproject xxx)：新建一个爬虫项目
- 明确目标(编写items.py)：明确你想抓取的目标
- 制作爬虫(spiders/xxspider.py)：制作爬虫开始爬取网页
- 存储内容(pipelines)：设计管道存储爬取内容

### 一、新建项目：(scrapy startproject)
- 开始爬取之前：创建名为mySpider的项目\
 `scrapy startproject muSpider`
 - 目录结构如下图所示：
 ![mySpider目录结构](file:///F:/ChromeDownLoad/Scrapy%E7%88%AC%E8%99%AB%E6%A1%86%E6%9E%B6/PythonSpider/file/images/7.2.png)
 - 简单说明主要文件的作用：
 > scrapy.cfg ：项目的配置文件\
mySpider/ ：项目的Python模块，将会从这里引用代码\
mySpider/items.py ：项目的目标文件\
mySpider/pipelines.py ：项目的管道文件\
mySpider/settings.py ：项目的设置文件\
mySpider/spiders/ ：存储爬虫代码目录

### 二、明确目标(mySpider/items.py)
- 抓取传智播客官网(http://www.itcast.cn/channel/teacher.shtml )上的所有讲师的信息。
    - 打开mySpider目录下的items.py
    - item定义结构化数据字段，用来保存爬取到的数据，有点像python中的dict，但是提供了一些额外的保护减少错误。
    - 可以通过创建一个scrapy.item类，并定义类型为scrapy.Field的类属性来定义一个Item（可以理解成类似于ORM的映射关系）。
    - 接下来，创建一个DemoItem类，和构建item模型（model）。
```python
import scrapy

class ItcastItem(scrapy.Item):
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
```

### 三、制作爬虫(spiders/itcastSpider.py)
- 爬虫主要分二步：
#### 1. 爬数据
- 在当前目录下输入命令，将在`mySpider/spiders`目录下创建一个名为itcast的爬虫，并制定爬取域的范围：\
`scrapy genspider itcast "itcast.cn"`
- 打开`mySpider/spiders`目录里面的itcast.py，默认增加以下代码：
```python
import scrapy

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = (
        'http://www.itcast.cn/',
    )

    def parse(self, response):
        pass
```
**其实也可以由我们自行创建itcast.py并编写上面的代码，只不过使用命令可以免去编写固定代码的麻烦**
- 要建立一个Spider， 你必须用scrapy.Spider类创建一个子类，并确定了三个强制的属性 和 一个方法。
    - `name = ""` ：这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。
    - `allow_domains = []`是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略。
    - `start_urls = ()` ：爬取的URL元祖/列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成。
    - `parse(self, response)`：解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数，主要作用如下：
        1. 负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
        2. 生成需要下一页的URL请求。
#### 2. 取数据
- 整个网页爬取完了，接下来就是取出数据的过程了
    - 之前在`mySpider/items.py`里定义了一个ItemsItem类，**需要在这里引进来，并且需要注意的是items里面定义的数据名称要与下面返回的items里面的名称一致！**
```python
from mySpider.items import ItcastItem

def parse(self, response):
    #open("teacher.html","wb").write(response.body).close()

    # 存放老师信息的集合
    items = []

    for each in response.xpath("//div[@class='li_txt']"):
        # 将我们得到的数据封装到一个 `ItcastItem` 对象
        item = ItcastItem()
        #extract()方法返回的都是unicode字符串
        name = each.xpath("h3/text()").extract()
        title = each.xpath("h4/text()").extract()
        info = each.xpath("p/text()").extract()

        #xpath返回的是包含一个元素的列表
        item['name'] = name[0]
        item['title'] = title[0]
        item['info'] = info[0]
        # name、title、info 这三个item名字与items.py文件里面保持一致
        items.append(item)

    # 直接返回最后数据
    return items
```  
- 保存数据：\
**scrapy保存信息的最简单的方法主要有四种，-o 输出指定格式的文件，命令如下：**
```python
# json格式，默认为Unicode编码
scrapy crawl itcast -o teachers.json

# json lines格式，默认为Unicode编码
scrapy crawl itcast -o teachers.jsonlines

# csv 逗号表达式，可用Excel打开
scrapy crawl itcast -o teachers.csv

# xml格式
scrapy crawl itcast -o teachers.xml
```

### 四、Item Pipeline
- 当Item在Spider中被收集之后，它将会被传递到Item Pipeline，这些Item Pipeline组件按定义的顺序处理Item。

- 每个Item Pipeline都是实现了简单方法的Python类，比如决定此Item是丢弃而存储。以下是item pipeline的一些典型应用：

    - 验证爬取的数据(检查item包含某些字段，比如说name字段)
    - 查重(并丢弃)
    - 将爬取结果保存到文件或者数据库中

- 编写item pipeline很简单，item pipiline组件是一个独立的Python类，其中process_item()方法必须实现:
```python
import something

class SomethingPipeline(object):
    def __init__(self):    
        # 可选实现，做参数初始化等
        # doing something

    def process_item(self, item, spider):
        # item (Item 对象) – 被爬取的item
        # spider (Spider 对象) – 爬取该item的spider
        # 这个方法必须实现，每个item pipeline组件都需要调用该方法，
        # 这个方法必须返回一个 Item 对象，被丢弃的item将不会被之后的pipeline组件所处理。
        return item

    def open_spider(self, spider):
        # spider (Spider 对象) – 被开启的spider
        # 可选实现，当spider被开启时，这个方法被调用。

    def close_spider(self, spider):
        # spider (Spider 对象) – 被关闭的spider
        # 可选实现，当spider被关闭时，这个方法被调用
```

#### 记录遇到的问题
- 当使用pipeline保存数据的时候出现了  
`TypeError: a bytes-like object is required, not 'str'`

出现该错误往往是通过open()函数打开文本文件时，使用了‘rb’或者‘wb’属性，如：fileHandle=open(filename,'rb'),则此时是通过二进制方式打开文件的，所以在后面处理时如果使用了str()函数，就会出现该错误，该错误不会再python2中出现。

具体的解决办法有以下二种：
1. 在open()函数中使用‘r’属性，即文本方式读取，而不是‘rb’,以二进制文件方式读取，可以直接解决问题。
2. 在open()函数中使用‘rb’,可以在使用之前进行转换，有以下实例，来自：http://stackoverflow.com/questions/33054527/python-3-5-typeerror-a-bytes-like-object-is-required-not-str

- 几个常用的scrapy的命令
```python
# 创建一个新的Scrapy项目：
scrapy startproject mySpider

# 制作爬虫：创建爬虫代码文件，并指定爬取域范围
# itcast 为创建的文件名 实际上会创建一个itcast.py
# "itcast.cn" 为指定的爬取域名
scrapy genspider itcast "itcast.cn"

# 运行
# 一个Scrapy爬虫项目里，可以存在多个爬虫。各个爬虫在执行时，就是按照 name 属性来区分
scrapy crawl itcast

# 启动Scrapy Shell
scrapy shell "http://www.itcast.cn/channel/teacher.shtml"

# 通过下面的命令可以快速创建 CrawlSpider模板的代码：
scrapy genspider -t crawl tencent tencent.com
```    
    

    

