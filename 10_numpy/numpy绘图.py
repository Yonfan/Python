#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-06 09:49:46
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np
import matplotlib.pyplot as plt

a = np.arange(12)
print(a)
# b = np.floor(np.random.rand(12)*5)
b = 2 * a + np.floor(np.random.rand(12) * 5)
print(b)

plt.scatter(a, b)
plt.show()
