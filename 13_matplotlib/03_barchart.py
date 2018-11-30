# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib

# 设置中文字体
matplotlib.rcParams['axes.unicode_minus'] = False
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['font.family'] = 'sans-serif'

plt.bar([1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label="条形图1", align="center")
plt.bar([2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label="条形图2", color="g")

plt.xlabel('数量')
plt.ylabel('高度')

plt.title('条形图实例')

plt.legend()
plt.show()
