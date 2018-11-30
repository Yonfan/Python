# -*- coding: utf-8 -*-

import re

# 正常的切分代码 无法识别连续的空格
print("a b c     d".split(' '))

# 使用正则表达式
pattern = re.compile(r'\s+')
res = pattern.split("a b c     d")
print(res)

# 也可以这样写
res = re.split(r'\s+', "a b c     d")
print(res)

# 当有多个其他的字符时候
res = re.split(r'[\s\;\,]+', "a ,b; c,   ;  d")
print(res)






