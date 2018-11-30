# -*- coding: utf-8 -*-
"""
先尝试用默认配置在同一张图上绘制正弦和余弦函数图像，然后逐步美化它。
    pylab 是 matplotlib 面向对象绘图库的一个接口。
"""

import numpy as np
import matplotlib.pyplot as plt

# X 是一个 numpy 数组，包含了从 −π 到 +π 等间隔的 256 个值。C 和 S 则分别是这 256 个值对应的余弦和正弦函数值组成的 numpy 数组。
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C,label="cos(x)")
plt.plot(X,S,label="sin(x)",color="g")

plt.legend()
plt.show()
