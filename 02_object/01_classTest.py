# -*- coding: utf-8 -*-
#(object)，表示该类是从哪个类继承下来的
# class Student(object):
# 	#__init__方法的第一个参数永远是self，表示创建的实例本身
# 	def __init__(self, name, score):
# 		self.name = name
# 		self.score = score

# bart = Student('YangFan',90)

# print('name:',bart.name)
# print('score:',bart.score)

# #数据封装
# def print_score(std):
# 	print('%s : %s' % (std.name, std.score))


# print_score(bart)

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s : %s' % (self.name,self.score))



bart = Student('YangFan',90)

bart.print_score()