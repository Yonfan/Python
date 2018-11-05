#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-05 15:18:10
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

# 给定间隔，间隔之外的值被剪切到间隔边缘。例如，如果指定[0， 1]的间隔，则小于0的值变为0，并且大于1的值变为1 。
import numpy as np
a = np.arange(10)
print('数组a为：')
print(a)
# 数值在1-8之间，不是的替换
print('clip给定数值在（1，8）也就是大于8的数值变为8，小于1的数值变为1')
print(np.clip(a, 1, 8))
print('=========================================')
print('数组a为：')
a = np.array([[1, 2], [3, 4]])
print(a)
print('mean整个数组的平均值：')
print(np.mean(a))
print('竖向平均值：')
print(np.mean(a, axis=0))
print('横向平均值：')
print(np.mean(a, axis=1))

print('=========================================')

a = np.array([[1, 2], [3, 4]])
print('数组a为：')
print(a)
print('数组平均值为：')
print(np.mean(a)) # 2.5
print('方差为 （样本值-平均值）的平方之和的平均值 ')
var = np.mean(abs(a - a.mean())**2)
print(var)
print('python 提供 var函数直接计算方差：')
print(np.var(a))

print('=========================================')

a = np.array([[1, 2], [3, 4]])
print('数组a为：')
print(a)
print('std标准差为方差var的平均根：')
print(np.sqrt(np.var(a)))
print('python 中利用std函数计算标准差：')
print(np.std(a))
print('竖向方差：')
print(np.var(a, axis=0))
print('竖向标准差：')
print(np.std(a, axis=0))
print('横向方差：')
print(np.var(a, axis=1))
print('横向标准差：')
print(np.std(a, axis=1))

print('=========================================')
a = np.array([[10, 7, 4], [3, 2, 1]])
print('数组a为：')
print(a)
print('median轴中值（就是中间的那个数，如果最中间为2个数则轴中值为他们的平均值）为：')
print(np.median(a))
print('竖向轴中值：')
print(np.median(a, axis=0))
print('横向轴中值：')
print(np.median(a, axis=1))
print('可以发现计算轴中值前会先将数组进行排序后再找中间的二个数：')
print(np.median([1,10,3,8]))
print(np.median([1,10,8]))