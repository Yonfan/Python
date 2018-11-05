#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-29
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

print(Month.Jan)

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

print('==============================')

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

print(Weekday.Mon)

print(Weekday.Tue)

print(Weekday['Tue'])

print(Weekday.Tue.value)

print(Weekday(1))