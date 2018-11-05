#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-30
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$

''' 自定义异常处理类 '''
class FooError(ValueError):
	"""docstring for FooError"""
	pass

def foo(s):
	n = int(s)
	if n==0:
		raise FooError('invaild value : %s' % s	)
	return 10 / n

foo('0')


