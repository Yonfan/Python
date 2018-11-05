#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-30
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$

from io import BytesIO

f = BytesIO()

l1 = f.write('中文'.encode('utf-8'))

print('l1 length = ', l1)

print('Value = ', f.getvalue())

print('==================input from BytesIO========================\n')

input = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')

inp = input.read()

print(inp)

