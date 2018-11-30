# -*- coding: utf-8 -*-

import re

pattern = re.compile(r'\d+')  # 用于匹配至少一个数字

m = pattern.match("one12twothree34four")  # 查找头部，没有匹配

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
# print(m)

# 上述的写法可以简写这样
m = re.match(r'\d+', "one12twothree34four")
print(m)

m = pattern.match("one12twothree34four", 2, 10)  # 从下标为2开始 也就是'e'的位置开始匹配，没有匹配
# print(m)

m = pattern.match("one12twothree34four", 3, 10)  # 从'1'的位置开始匹配，正好匹配
print(m)

print(m.group())   # 查看匹配的字符串

print(m.start())    # 查看匹配的开始位置下标

print(m.end())      # 查看匹配的结束位置下标

print(m.span())     # 查看匹配到的字符串的区间下标




