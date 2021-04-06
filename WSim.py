# -*- coding: UTF-8 -*-
"""
@author:dodio
@description:
@file:WSim.py
@time:2021/04/03
"""

import numpy as np
import matplotlib.pyplot as plt
from scripts import WsimScr as Ws
import time

unit_num = 50
unit_weath = 100
units = [100 for x in range(0, unit_num)]
year = 5
t1 = time.perf_counter()
Ws.YearChag(units, year, unit_weath)  # 单位年演化
t2 = time.perf_counter()

units_sort = units.copy()  # 重新排序
units_sort.sort()
ax = np.arange(0, unit_num, 1)
# plt.subplot(2, 1, 1)
plt.bar(ax, units, alpha=0.5)
# plt.subplot(2, 1, 2)
plt.bar(ax, units_sort, alpha=0.7)
plt.show()
print(t2 - t1)
