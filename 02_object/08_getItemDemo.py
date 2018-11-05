#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-29
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$

# -*- coding: utf-8 -*-
class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		self.a, self.b = 0, 1  						#初始化数值

	def __iter__(self):		
		return self									#实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b  	# 计算下一个值
		if self.a > 10000:							# 退出循环的条件				
			raise StopIteration()					
		return self.a								# 返回下一个值

	def __getitem__(self, n):
		if isinstance(n, int):						# n是索引
			a, b = 1, 1
			for x in range(100):
				a, b = b, a+b
			return a
		if isinstance(n, slice):					# n是切片
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1 
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a+b 
			return L


# 是list有个神奇的切片方法：list(range(100))[5:10]

# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断

print(Fib()[0:5])
print(Fib()[0:10])
print(Fib()[:])