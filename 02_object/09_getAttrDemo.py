#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Student(object):

    def __init__(self):
        self.name = 'Michael'
# 当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr=='age':
            return lambda: 25  #返回函数也可以
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


print(Student().abc())