# -*- coding: utf-8 -*-

# 享学课堂-老郭（图例、标题和标签）
import matplotlib.pyplot as plt
import matplotlib
# 设置中文字体
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

plt.plot(x, y, label='第一条线')
plt.plot(x2, y2, label='第二条线')

plt.xlabel('x轴标签')
plt.ylabel('y轴标签')
plt.title('享学课堂-matplotlib教程')
plt.legend()
plt.show()