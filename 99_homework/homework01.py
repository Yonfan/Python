#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-02 17:01:55
# @Author  : YF (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np

# strnum = input('请输入一个字符串：')
# print('输入的字符串为：', strnum)

s="1,2,3"
i=np.array([int(c) for c in s.split(",")])
print(i)
maxlen=len(bin(max(i)))
b=["0"*(1+maxlen-len(bin(j)))+bin(j)[2:] for j in i]
print(b)
res=[[int(l) for l in k] for k in b]
print(res)
