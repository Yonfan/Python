#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-29
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

# call方法感觉有点像java中的构造函数 实例化一个对象的时候就会默认调用该方法的构造函数

s=Student('YangFan')
s()

# 对象可以看成函数，函数也可以看成对象， 那么怎么判断一个变量是函数还是对象？ 
# 其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象

print('Student(\'xxx\')',callable(Student('xxx')))
print('max',callable(max))
print('[1,2,3]',callable([1, 2, 3]))
print('None',callable(None))
print('str',callable('str'))