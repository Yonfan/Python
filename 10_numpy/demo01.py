#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-02 12:34:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np

a = np.arange(12)
print(a.shape)
a = a.reshape(3, 4)
print(a)
print(a.shape)
print(type(a))

print('=======================')
# reshape(m , n) 必须得满足 m*n = size
b = np.arange(15).reshape(3, 5)
print('b = ', b)
# colunm and
print('b.shape = ', b.shape)
# 维度
print('b.ndim = ', b.ndim)
# 数据类型
print('b.dtype.name = ', b.dtype.name)
# item 长度 4
print('b.itemsize = ', b.itemsize)
# 长度
print('b.size = ', b.size)

print('==========三维数组？？=========')

c = np.arange(8).reshape(2, 2, 2)

print('c = ', c)

print('==========使用array创建数组=========')

d = np.array([1, 2, 3, 4, 5])
print('d = ', d)

print('tyep(d) = ', type(d))

e = np.array([(1, 2, 3, 4), (5, 6, 7, 8)])

print('e = ', e)

print('==============================其他方法创建数组============================')
print('==========创建具有初始化占位符内容数组=========')
f = np.zeros((2, 3))
print('全 0 np.zeros((2,3)) = ', f)
print('全 1 np.ones((2,3)) = ', np.ones((2, 3)))
print('默认全1 np.empty((2,3)) = ', np.empty((2, 3)))

print('arange 整型 np.arange(1,10,2) : ', np.arange(1, 10, 2))

print('arange 浮点型 np.linspace(1,2,5)', np.linspace(1, 2, 5))

print('\nzeros_like/ones_like 和另外一个矩阵相似，但是值全为0/1')

m = np.arange(6).reshape(2, 3)
print(' m : ', m)
m = np.zeros_like(m)
print('np.zeros_like(m) : \n', np.zeros_like(m))

n = np.random.rand(2, 3)
print('np.random.rand : \n', n)

l = np.eye(3)
print('np.eye(3) :\n ', l)
