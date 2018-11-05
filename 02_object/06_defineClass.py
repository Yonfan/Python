# -*- coding: utf-8 -*-
class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name
	def __str__(self):			#感觉有点像java中的toString函数				
		return 'Student object (name : %s)' % self.name
	# __repr__ = __str__

print('invocate __str__ : ',Student('YangFan'))

s = Student('hello')

print('invocate __repr__ : ',type(s)) 