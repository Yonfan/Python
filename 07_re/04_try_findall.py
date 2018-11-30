# -*- coding: utf-8 -*-

import re

pattern = re.compile(r'\d+')  # 查找多个数字

res = pattern.findall('Hello 12345 789')
print(res)

pattern1 = re.compile(r'\d')  # 查找单个数字
res = pattern1.findall('Hello 12345 789')
print(res)

res2 = pattern.findall('one1two2three3four4', 0, 10)    # 查找指定区间里面至少一个或无限个
print(res2)



