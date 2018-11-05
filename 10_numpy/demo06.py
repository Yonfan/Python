#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-04 10:36:24
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np

print('===========all:只要数组中有有一个为False则为False 相当与逻辑运算中的 与 and &=================')

a = np.all([[True, False],[True, True]])
print(a)

a = np.all([[True, False],
			[True, True]], axis=0)

print(a)

a = np.all([-1,4,5])

print(a)

print('===========any:只要数组中有有一个为True则为True=================')

a= np.any([[True, False],[True, True]])

print(a)

a = np.any([[True, False], [False, False]], axis=0)
print(a)

a = np.any([-1, 0, 5])
print(a)

a = np.zeros((2, 3),dtype=int)
print(a)
print(np.any(a))

a = np.eye((3),dtype=int)
print(a)
print(np.any(a))




# 0相当于False
while 0:  
	print(2)
	break