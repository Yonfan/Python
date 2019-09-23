# -*- coding: utf-8 -*-

# 导入Numpy
import numpy as np

# 创建数组
a = np.array([1, 2, 3, 4])  # list
print(a)
print(a.shape)
b = np.array((1, 2, 3, 3))  # tuple
print(b)
print(b.shape)
c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [7, 8, 9]])  # list类型的多维数组
print(c)
print(c.dtype)  # dtype获取数组的元素类型
print(c.shape)  # shape获取数组的大小
c.shape = (3, 4)  # 改变数组的形状
print(c)
c.shape = 2, -1  # 自动修正数组的形状
print(c)
print("*" * 100)

# arange
e = np.arange(0, 1, 0.1)
print(e)
print(e.dtype)
e = np.arange(0, 1, 0.1, int)
print(e)
print(e.dtype)
print("*" * 100)

# linspace
f = np.linspace(0, 1, 10)
print(f)
f = np.linspace(0, 1, 10, endpoint=False)
print(f)

print("*" * 100)
# linspace
g = np.logspace(0, 2, 20)

# 产生布尔数组
x = np.random().rand(10) > 0.5

# 多维数组
np.dtype({'names':['name', 'age', 'weight'], 'formats':('S32', 'i', 'f')})
