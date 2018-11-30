# -*- coding: utf-8 -*-

import re

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写

m = pattern.match('Hello World Wide Web')

print(m)

print(m.span())
print(m.group(0))  # 返回匹配成功的整个子串
print(m.span(0))  # 返回匹配成功的整个子串的索引
print('*' * 10)
print(m.group(1))  # 返回第一个分组匹配成功的子串
print(m.span(1))  # 返回第一个分组匹配成功的子串的索引
print('*' * 10)
print(m.group(2))  # 返回第二个分组匹配成功的子串
print(m.span(2))  # 返回第二个分组匹配成功的子串的索引
# print(m.group(3))

print('*' * 10)  # 等价于 (m.group(1), m.group(2), ...)
print(m.groups())
