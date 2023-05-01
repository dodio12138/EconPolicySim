# -*- coding: UTF-8 -*-
"""
@author:dodio
@description:
@file:MPTools.py
@time:2021/10/22
"""
import random


# 省份类
class stateInfo:
    '名称|土地规模|资产阶级规模|无产阶级规模'

    def __init__(self, name, land, bourgeois, proletariate):
        self.name = name
        self.land = land
        self.bourgeois = bourgeois
        self.proletariate = proletariate


# 生产率类
class productivity:
    '国家|社会|资产阶级|无产阶级'

    def __init__(self, country, social, bourgeois, proletariate):
        self.country = country
        self.social = social
        self.bourgeois = bourgeois
        self.proletariate = proletariate


# 生产关系
def ProductionRelations(type, stateInfo, productivity):
    if type == 0:
        production = stateInfo.land * stateInfo.proletariate * (
                productivity.bourgeois + productivity.proletariate) * productivity.social
    elif type == 1:
        production = stateInfo.land * stateInfo.proletariate * productivity.proletariate * productivity.social
    else:
        production = stateInfo.land * stateInfo.proletariate * productivity.social * productivity.country
    return round(production, 2)
