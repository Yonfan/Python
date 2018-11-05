#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-30
# @Author  : ${author} (${email})
# @Link    : ${link}
# @Version : $Id$

import os

print('''如果是posix，说明系统是Linux、Unix或Mac OS X，
如果是nt，就是Windows系统。''')

print('os.name = ', os.name)

print('要获取详细的系统信息，可以调用uname()函数：')

try:
	print('os.uname = ', os.uname())
except AttributeError as e:
	print('uname()函数在Windows上不提供')


print('''操作系统中定义的环境变量，
全部保存在os.environ这个变量''')
# print('os.environ = ',os.environ )
print(r"os.environ.get('JAVA_HOME') = ",os.environ.get('JAVA_HOME'))

