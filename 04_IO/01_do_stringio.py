#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-30
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$

from io import StringIO

f = StringIO()

s1 = f.write('hello')
# 返回的是写入的长度
print(s1)

s2 = f.write('    ')

print(s2)

s3 = f.write('world')

print(s3)

print(f.getvalue())

print('================Read From StringIO==================')

input = StringIO('Hello!\nHi!\nGoodbye!')

while 1:
	s = input.readline()
	if s == '':
		break
	print(s.strip())

