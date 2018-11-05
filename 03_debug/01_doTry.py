#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-30
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$

try:
	print('try...')
	r = 10 / 0 
	print('result : ', r)
except ZeroDivisionError as e:
	print('except : ', e)
	raise e
finally:
	print('Finally ...')
print('END')




