#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-05 16:23:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np

print('reshape 转换形状操作：')
a = np.arange(12).reshape(3, 4)
print(a)
print(a.shape)

print('ravel 将多维数组转换成一维数组：')
b = a.ravel()
print(b)

print('.T 将矩阵进行转置：')
c = a.T
print(c)

print('resize 将原来形状的矩阵修改成新的形状的矩阵：')
a.resize(2, 6)
print(a)

print('vstack/hstack 垂直堆叠/水平堆叠：')
print('vertical：垂直；horizontal：水平 ')
a = np.array([(1, 2, 3),(4, 5, 6)])
print('矩阵a为：')
print(a)
b = np.array([(10, 20, 30),(40, 50, 60)])
print('矩阵b为：')
print(b)
print('垂直堆叠后的a，b形成新的矩阵：')
c = np.vstack((a, b))
print(c)
print('水平堆叠后的a，b形成新的矩阵：')
d = np.hstack((a, b))
print(d)
print('那么问题来了？这时的a，b形状一样，如果形状不一样回事什么结果呢？')
print('将b转换成（3，2）')
b = b.reshape(3,2)
print('转换后的矩阵b为：')
print(b)
print('会报报数组维度不匹配的错误！')
# 会报报数组维度不匹配的错误！
# print('水平堆叠后的a，b形成新的矩阵：')
# c = np.vstack((a, b))
# print(c)
# print('垂直堆叠后的a，b形成新的矩阵：')
# d = np.hstack((a, b))
# print(d)
print('column_stack 根水平堆叠有点像')
a = np.array([(1, 2, 3),(4, 5, 6)])
b = np.array([(10, 20, 30),(40, 50, 60)])
print('数组a为：')
print(a)
print('数组b为：')
print(b)
print('column_stack((a,b)):')
print(np.column_stack((a, b)))
print('拆分hsplit/vsplit/array_split(指定轴)')
a = np.floor(10*np.random.random((2,12)))
print('随机数组a(2,12):')
print(a)
print('hsplit(a,3)将a横向划分为3组，相当于a为一块蛋糕，现在用一把刀把a水平切割成3组：')
print(np.hsplit(a, 3))
print('vsplit(a,2)将a竖向划分为2组：')
print(np.vsplit(a,2))
print('那么能不能将a竖直划分为3组呢？np.vsplit(a,3),由于a本身是(2,12)2行12列的,所以竖直方向上划分3行是会抛异常的！')
print('使用numpy.array_split(ary, indices_or_sections, axis=0)划分,默认竖直划分')
print(np.array_split(a,2))
print(np.array_split(a,3))

