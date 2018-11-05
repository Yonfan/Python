#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-05 16:13:13
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np

a = np.arange(10)**3
print('数组a为：')
print(a)
print('数组a[2]为：')
print(a[2])
print('数组a[2：6]为：')
print(a[2:6])

# 遍历
print('遍历数组a:')
for x in a:
	print(x)

print('========================================')
a = np.arange(12).reshape(3, 4)
print('数组a为：')
print(a)
# 第1行，第2列，索引从0开始
print('第一行，第二列.a[1,2] : ')
print(a[1,2])
# 第二列的所有
print("a[:1]:(第二列的所有)")
print(a[:,1])
print('a[1]：(第二行的所有)')
print(a[1])
# 迭代
print('迭代打印出每一行：')
for row in a:
	print(row)
print('--------------')
print('迭代打印出每一行的值：')
for row in a:
	for x in row:
		print(x, end=' ')
	print()