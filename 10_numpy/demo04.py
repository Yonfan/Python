#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-04 09:52:37
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np

a = np.ones((2,3), dtype=int)
print(a.dtype.name)
print(a)

b = np.random.random((2,3))
print(b.dtype.name)
print(b)

a *= 3
print(a)

b += a
print(b)

c = np.random.rand(2,3)
print(c)
print(c.dtype.name)

# 类型转换错误
# a += b 
# print(a)
