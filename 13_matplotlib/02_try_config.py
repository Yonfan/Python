# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family']='sans-serif'

# 年龄
population_ages = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
# 年龄区间，10岁为一个区间
bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')

plt.ylabel('y')

plt.title('享学课堂-matplotlib教程')

plt.legend()
plt.show()