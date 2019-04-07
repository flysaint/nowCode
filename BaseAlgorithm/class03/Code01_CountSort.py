# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:55:21 2019

@author: fly_s
计数排序
问题：将年龄排序，时间复杂度再O(N)

思路：年龄最多不超过200岁，创造200个桶，将年龄装进去，再依此取出

"""
import random

def countSort(arr):
    if arr is None or len(arr) < 2:
        return 
    
    maxAge = max(arr)
    
    helpArr = [0 for i in range(maxAge)]
    
    for n in arr:
        helpArr[n-1] = helpArr[n-1] + 1
    
    arr2 = []
    for i in range(len(helpArr)):
        while(helpArr[i] > 0):
            arr2.append(i + 1)
            helpArr[i] = helpArr[i] - 1
    return arr2
        

testArr = random.sample(range(200),10)

testArr = countSort(testArr)







