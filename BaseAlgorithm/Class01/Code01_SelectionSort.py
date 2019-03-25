# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:44:33 2019
@author: DELL
"""
import numpy as np
import pandas as pd
'''
选择排序
# TestCase：
# 原列表为：[54, 26, 93, 17, 77, 31, 44, 55, 20]
# 新列表为：[17, 20, 26, 31, 44, 54, 55, 77, 93]
思路：每次选择最小值到当前位置
1）外循环。从数组的第一个元素开始遍历。假设当前最小值下标外循环当前的下标。
2）内循环。从外循环后一个元素开始遍历，与当前外循环数值进行对比。如果内循环的数小于外循环的数，更换最小值下标。
完成一个完整的内循环后，再更换数值。
'''
def selectionSort(arr) :
    arrLen = len(arr)
    if (arr is np.nan or arrLen < 2):
        return
    for i in range(0,arrLen - 1): # 外循环 i ~ N-1 遍历
        minIndex = i
        for j in range(i + 1,arrLen): # 内循环 在 i ~ N-1 位置上，找最小值的下标 
            print("i = {} , j = {} ,minIndex = {}  ".format(i,j,minIndex))
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr = swap(arr, i, minIndex)
    return arr
def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    return arr
	
arrTest = [54, 26, 93, 17, 77, 31, 44, 55, 20]

arrSorted = selectionSort(arrTest)
len(arrTest)





