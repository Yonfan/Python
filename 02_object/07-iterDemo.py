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
		a, b = 1, 1
		for x in range(n):
			a , b  = b, a+b
		return a 


for x in Fib():
	print(x)



# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：

# >>> Fib()[5] 就会出现错误 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法

print('Fib()[5]  = ', Fib()[5])