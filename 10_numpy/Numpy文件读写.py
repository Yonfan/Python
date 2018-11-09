#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-05 20:44:52
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np

a = np.eye(3)
print(a)
# 保存为txt文件
np.savetxt('eye.txt', a)
print(np)
# 加载txt文件
print(np.loadtxt('eye.txt'))

# c,v = np.loadtxt('data.csv', delimiter=',', usecols=(6,7), unpack=True)
# print(v)

'''
加载数据，加载第六列和第七列到数组中。
'data.csv'：数据
delimiter：分隔符
usecols：元组加载第六列和第七列
unpack：(True)分开存储
 
CSV(Comma Separated Value, 逗号分隔值)
 
AAPL,28-01-2011, ,344.17,344.4,333.53,336.1,21144800
 0     1        2   3      4      5      6       7
代码，日期，空，开盘价，最高价，最低价，收盘价，日成交量
'''
