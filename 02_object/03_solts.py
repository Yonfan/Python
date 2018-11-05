# -*- coding: utf-8 -*-
class Student(object):
	__slots__ = ('name', 'age')# 用tuple定义允许绑定的属性名称




s = Student()
s.name = 'YangFan'
s.age = 22

print('name  = ',s.name ,'age = ', s.age )

# 添加限制之外的属性的时候就会报错，起到限制作用
s.score = 99