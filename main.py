# -*- coding: UTF-8 -*-
"""
@author:dodio
@description:
@file:main.py
@time:2021/04/02
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

length = 50
data = np.zeros((50, 1), dtype=float)
for i in range(length):
    data[i] = np.random.randint(0, 50)

pic = plt.figure()
ax = np.arange(1800, 1800 + length, 1)
plt.xlabel('年份', fontproperties='SimHei')
plt.ylabel('GDP')
plt.plot(ax, data)
plt.show()
