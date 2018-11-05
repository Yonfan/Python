#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-04 16:18:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np 

data = np.arange(6).reshape(3,2)
print(data)
# 每一行的第一个元素乘以weights[0] 第二个元素乘以weights[1] 
avg = np.average(data, axis=1, weights=[1./4, 3./4])
print(avg)
# 每一列的 第一个元素乘以weights[0] 依次类推
avg = np.average(data, axis=0, weights=[1./4, 2./4, 1./4])
print(avg)
