# -*- coding: UTF-8 -*-
"""
@author:dodio
@description:
@file:MPSim.py
@time:2021/10/22
"""

import matplotlib.pyplot as plt
import numpy as np
from scripts import MPTools
import random

mouth_count = 201
time = list(range(1, mouth_count))

# 社会信息参数
# 人口增长率
popRate = 0.01
# 历史人口数组
popNum = np.empty((mouth_count - 1))
# 科技增长率
sci_develop = 0.2

# 生产率
productivity = MPTools.productivity(1.2, 1.1, 2, 1.15)

# 省份信息
JiangSu = MPTools.stateInfo("江苏", 10, 4, 100)


def updata():
    for i in range(1, mouth_count - 1):
        # 更新社会信息参数
        # 更新省份信息
        randomNum = [-0.5, 0.5]  # 历史震荡系数
        productivity.social = productivity.social + random.uniform(randomNum[0], randomNum[1]) + sci_develop
        productivity.proletariate = productivity.proletariate + random.uniform(randomNum[0], randomNum[1])
        productivity.country = productivity.country + random.uniform(randomNum[0], randomNum[1]) + sci_develop
        productivity.bourgeois = productivity.bourgeois + random.uniform(randomNum[0], randomNum[1]) + sci_develop

        JiangSu.proletariate += JiangSu.proletariate * (1 + popRate)
        popNum[i] = JiangSu.proletariate


def production(production):
    for i in range(1, mouth_count - 1):
        if i == 0:
            production[i] = MPTools.ProductionRelations(0, JiangSu, productivity)
        else:
            production[i] = MPTools.ProductionRelations(0, JiangSu, productivity) + production[i - 1]


updata()
# 资本私有生产资料
production_0 = np.empty((mouth_count - 1))
production(production_0)

# 个人私有生产资料
production_1 = np.empty((mouth_count - 1))
production(production_1)

# 国家公有生产资料
production_2 = np.empty((mouth_count - 1))
production(production_2)

plt.figure(figsize=(10, 2.5))
plt.subplot(121)
plt.plot(time, production_0, label='BourgeoisPriOwn', color='tomato')
plt.plot(time, production_1, label='ProletariatePriOwn', color='lightblue')
plt.plot(time, production_2, label='CountryPubOwn', color='gold')
plt.xlabel('TIME/MONTH')
plt.ylabel('PRODUCTON')
plt.ylim(production_1[0] - 100)
plt.legend(loc='upper left')
# 人口图
plt.subplot(122)
plt.plot(time, popNum, label='JiangSu', color='black')
plt.xlabel('TIME/MONTH')
plt.ylabel('POPULATION')
plt.ylim(popNum[0])
plt.legend(loc='upper left')
plt.show()

print(popNum[1])
