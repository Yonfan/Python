#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-04 09:47:35
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np

a = np.array([[1,1],[0,1]])

b = np.array([[2,0],[3,4]])

print(a*b)

print(a.dot(b))

print(np.dot(a, b))

