#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-05 14:58:20
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np 

a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
print('原数组：')
print(a)
print('ceil向上取整：')
print( np.ceil(a))
print('floor向下取整：')
print(np.floor(a))
print('trunc返回输入的截断值（相当于取整数部分）:')
print(np.trunc(a))
print('rint舍入取整:')
print(np.rint(a))


