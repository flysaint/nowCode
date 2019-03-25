# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:10:08 2019
@author: fly_s
理解：逆向查牌。每次抽一张牌，挨个和前面的牌做对比
外循环。从 i = 1 ~ N -1。给出本次要进行 检查的牌
内循环。从 j = i ~ 0。本次要查的牌，和之前所有以查过的牌做对比。如果牌j < 牌 j-1，则进行交换
结束条件。因为之前牌都是排过序的，因此 牌j > 牌 j- 1，中止；或者 j == 0
"""
import numpy as np
import pandas as pd
def swap(v1,v2):
    v1 = v1^v2
    v2 = v1^v2
    v1 = v1^v2
    return v1,v2

def InsertSort(arr):
    if(arr is np.nan or arr is None or len(arr) < 2):
        return 
    else:
        arrLen = len(arr)
        for i in range(1,arrLen):
            for j in range(i,0,-1):
                #print("i = {},j = {}".format(i,j))
                if arr[j] < arr[j-1]:
                    arr[j],arr[j-1] = swap(arr[j],arr[j-1])
        return arr
                
arrTest = [54, 26, 93, 17, 77, 31, 44, 55, 20]
len(arrTest)

arrSorted = InsertSort(arrTest)

"""
对数器的概念和使用
1，有一个你想要测的方法a
2，实现复杂度不好但是容易实现的方法b
3，实现一个随机样本产生器
4，把方法a和方法b跑相同的随机样本，看看得到的结果是否一样。
5，如果有一个随机样本使得比对结果不一致，打印样本进行人工干预，改对方法a或者
方法b
6，当样本数量很多时比对测试依然正确，可以确定方法a已经正确。
"""
# 生成随机库
# 记得带对数器上考场
import random

def isEqual(arr1,arr2):
    if((arr1 is None and arr2 is not None) or (arr1 is not None and arr2 is None )):
        return False
    if(arr1 is None and arr2 is None):
        return True
    arr1Len = len(arr1)
    arr2Len = len(arr2)
    if( arr1Len != arr2Len):
        return False
    for i in range(arr1Len):
        if(arr1[i] != arr2[i]):
            return False
    return True

testTime = 5000
maxSize = 100
maxValue = 100
for i in range(0,testTime):
    testArr1 = random.sample(range(0,testTime),maxSize)
    testArr2 = testArr1.copy()
    testArr1 = InsertSort(testArr1)
    (testArr2).sort()
    if not isEqual(testArr1,testArr2):
        print('bad Job!')
    
    
    
    
    
    
    
    
    
    
    
    
    
    