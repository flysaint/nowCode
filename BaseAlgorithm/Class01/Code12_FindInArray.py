# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:28:39 2019
@author: fly_s
一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，
判断数组中是否含有该整数。
"""
import numpy as np
import pandas as pd
import random

arrs = np.array([1,2],[2,3])

arrs = [random.sample(range(0,100),3) for i in range(3)]

def findInArray(arrs,target):
    if arrs is None:
        return target is None
    for arr in arrs:
        if target in arr:
            return True
    return False


findInArray(arrs,34)

