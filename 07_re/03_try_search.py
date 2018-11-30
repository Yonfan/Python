# -*- coding: utf-8 -*-

'''
search 方法用于查找字符串的任何位置，它也是一次匹配，只要找到了一个匹配的结果就返回，而不是查找所有匹配的结果
'''

import re

pattern = re.compile(r'\d+')

m = pattern.search('one12twothree34four')
# print(m)
# print(m.group())

m = pattern.search('one12twothree34four', 10, 30)  # 指定字符串区间
# print(m)
# print(m.group())


# 使用 search() 查找匹配的子串，不存在匹配的子串时将返回 None
m = pattern.search('Hello 12345 789')

if m:
    # 使用 Match 获得分组信息
    print('matching string:', m.group())
    # 起始位置和结束位置
    print('position:', m.span())
