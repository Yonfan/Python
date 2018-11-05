#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-03 15:51:05
# @Author  : YF (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np

ndim5 = np.random.randint(0, 100, size = (5, 5))
print(ndim5)
nmax, nmin = ndim5.max(), ndim5.min()
print(nmax, nmin)
ndim5 = (ndim5 - nmin)/(nmax - nmin)
print(ndim5)