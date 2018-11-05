#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-04 16:27:30
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np 
print('返回数组的排序副本')
a = np.array([[1,4],[3,1]])
print(np.sort(a))
# 拉直为一维数组，再排序
print(np.sort(a, axis=None))
# 沿着纵轴排序
print(np.sort(a, axis=0))
# 沿着横轴排序
print(np.sort(a, axis=1))
print('=================================')
print('argmax/argmin返回沿轴的最大/最小值的索引，注意返回的的索引！')
a = np.arange(6).reshape(2,3)
print(a)
print(np.argmax(a))
print(np.argmax(a, axis=0))
print(np.argmax(a, axis=1))

print(np.argmin(a))
print(np.argmin(a, axis=0))
print(np.argmin(a, axis=1))
print('=================================')
print('argsort 返回将数组排序的索引')
x = np.array([5, 3, 8])
print(np.argsort(x))

# 二维
x = np.array([[0, 3], [2, 2]])
print(np.argsort(x, axis=0))


print(np.argsort([5,3,8]))
