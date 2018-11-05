#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-04 10:17:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np

a = np.random.random((2,3))

print(a)

print(a.sum())

print(a.min())

print(a.max())


b = np.arange(12).reshape(3,4)
print(b)
print('===========================')
# 列的和
print(b.sum(axis=0))
# # 行的和
print(b.sum(axis=1))
print('===========================')
# 每行累加和
print(b.cumsum(axis=1))
print()
print(b.cumsum(axis=0))