#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-06 18:20:58
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# 下面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：

# environ：一个包含所有HTTP请求信息的dict对象；

# start_response：一个发送HTTP响应的函数。

def application(environ, start_response):
    start_response([('Content-Type', 'text/html')], '200 OK')
    # print(environ['REQUEST_METHOD'])
    # print(environ['User-Agent'])
    # print(environ)
    body = '<h1>Hello, %s!</h1>' % (environ["REQUEST_METHOD"] or 'web')
    # body = "<h1>Hello, lalall!</h1>"
    return [body.encode('utf-8')]
