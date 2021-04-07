# -*- coding: UTF-8 -*-
"""
@author:dodio
@description:
@file:WsimScr.py
@time:2021/04/03
"""
import numpy as np


def WealthCurrency(list_WC, i, weath):
    isDebt = 0
    list_RT = RandomTrend(list_WC, weath)
    if list_WC[i] > 0 or isDebt:
        list_WC[i] -= (weath / 100)
        list_sort_WC = list_WC.copy()
        list_sort_WC.sort()
        list_WC[list_WC.index(np.random.choice(list_sort_WC, p=np.array(list_RT).ravel()))] += (weath / 100)
    else:
        pass


def RandomTrend(list_RT, weath):
    list_sort_RT = list_RT.copy()
    list_sort_RT.sort()
    i = 0
    while i < len(list_RT):
        if list_sort_RT[i] > 0:
            list_sort_RT[i] = list_sort_RT[i] / (len(list_RT) * weath)
        i += 1
    return list_sort_RT


def YearChag(list_, year, weath):
    for i in range(0, int(364 * year)):  # i为一天
        for j in range(len(list_)):  # j为单位index
            WealthCurrency(list_, j, weath)
