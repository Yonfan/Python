# -*- coding: utf-8 -*-
'''回忆一下Animal类层次的设计，假设我们要实现以下4种动物：
	Dog - 狗狗；
	Bat - 蝙蝠；
	Parrot - 鹦鹉；
	Ostrich - 鸵鸟。

	分类可以飞，可以跑
	分类哺乳动物，鸟类

	哺乳类：能跑的哺乳类，能飞的哺乳类；
	鸟类：能跑的鸟类，能飞的鸟类。
	'''
# 基类
class Animal(object):
	pass

# 大类:
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Bird, Flyable):
    pass

class Ostrich(Bird, Runnable):
    pass