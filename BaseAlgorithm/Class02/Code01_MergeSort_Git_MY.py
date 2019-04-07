# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:25:26 2019
@author: DELL
****************************
****主要：一天的心得。********
****************************
1. 把每一层设置FLag。所谓递归就是树结构，把结构看清楚了就没问题。
2. Python 和 Java 有些不同。牛客的案例中，java是直接对队列进行全局的操作。
"""
import os
os.chdir(r'D:/Code/github/nowCode/nowCode/BaseAlgorithm/Class02/')
from Utils import * 
import random

import operator


def mergSort(lst):
    if len(lst) == 1:
        return lst
    mid = int(len(lst)/2)
    LeftLst = mergSort(lst[:mid])
    RightLst = mergSort(lst[mid:])
    return merg(LeftLst,RightLst)


def merg(LeftList,RightList):
    p1 = 0
    p2 = 0
    helpArr = []
    while(p1 <= len(LeftList) - 1 and p2 <= len(RightList) - 1):
        if(LeftList[p1] <= RightList[p2]):
            helpArr.append(LeftList[p1])
            p1 = p1 + 1
        else:
            helpArr.append(RightList[p2])
            p2 = p2 + 1
    while(p1 <= len(LeftList) - 1):
        helpArr.append(LeftList[p1])
        p1 = p1 + 1
    while(p2 <= len(RightList) - 1):
        helpArr.append(RightList[p2])
        p2 = p2 + 1
    return helpArr


testArr = [1,5,3]


testArr1 = random.sample(range(0,100),50)
testArr2 = testArr1.copy()


for i in range(0,100):
    if not (operator.eq(mergSort(testArr1),sorted(testArr2))):
        print('bad')
        print(testArr1)
        break

mergSort(testArr)

merg([1,4,5],[3,8,15])













