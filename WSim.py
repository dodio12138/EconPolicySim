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

unit_num = 150
unit_weath = 100
units = [100 for x in range(0, unit_num)]
year = 0
# t1 = time.perf_counter()
while year < 3.1:
    Ws.YearChag(units, year, unit_weath)  # 单位年演化
    # t2 = time.perf_counter()
    units_sort = units.copy()  # 重新排序
    units_sort.sort()
    ax = np.arange(0, unit_num, 1)
    plt.bar(ax, units_sort, alpha=0.7, color='red')
    plt.text(2, 2500, 'YEAR: ' + str(int(round(year * 10))))
    year += 0.1
    print(year)
    plt.ylim(0, 3000)
    plt.ylabel('WEALTH')
    plt.xlabel('INDEX')
    plt.savefig('Filter_' + str(int(round(year * 10))) + '.png', dpi=100)
    plt.show()
    units = [100 for x in range(0, unit_num)]

# plt.subplot(2, 1, 1)
# plt.bar(ax, units, alpha=0.5)
# plt.subplot(2, 1, 2)


# print(t2 - t1)
