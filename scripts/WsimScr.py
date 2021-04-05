# -*- coding: UTF-8 -*-
"""
@author:dodio
@description:
@file:WsimScr.py
@time:2021/04/03
"""
import numpy as np


def WealthChag(list, i):
    isDebt = 0
    if list[i] > 0 or isDebt:
        list[i] -= 100
        list[np.random.randint(0, len(list))] += 100
    else:
        pass


def YearChag(list, year):
    for i in range(0, 364 * year):  # i为一天
        for j in range(len(list)):  # j为单位index
            WealthChag(list, j)
