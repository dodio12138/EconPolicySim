# -*- coding: UTF-8 -*-
"""
@author:dodio
@description:
@file:main.py
@time:2021/04/02
"""

import numpy as np
import matplotlib.pyplot as plt

data = []
for i in range(50):
    data.append(np.random.randint(0, 50))

pic = plt.figure()
ax = np.arange(0, 50, 1)
plt.plot(ax, data)
plt.show()
