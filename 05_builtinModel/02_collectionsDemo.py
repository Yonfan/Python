#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-01 10:20:44
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from collections import namedtuple

# 定义特定的数据类型
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p)

from collections import deque
# 双向列表 适用于栈和队列
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

from collections import defaultdict
# 希望dict的key不存在时不抛出KeyError而是返回一个默认值
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'asss'
print(r"dd['key1'] = ",dd['key1'])
print(r"dd['kkk'] = ",dd['kkk'])

from collections import OrderedDict
# 在对key做迭代的时候希望dict有序 也就是插入是什么顺序读出来也是这个顺序
d = dict([('a', 1),('c', 3),('b', 2),('d', 4)])
print('d = ', d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print('od = ', od)

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
ll = list(od.keys()) # 按照插入的Key的顺序返回
print('ll =', ll)

# 用OrderDict实现一个先进先出的dict，当超出容量的时候先删除最早添加的Key

