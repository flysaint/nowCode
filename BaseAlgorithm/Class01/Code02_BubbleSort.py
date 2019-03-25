# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:46:34 2019
@author: fly_s
选择排序
# TestCase：
# 原列表为：[54, 26, 93, 17, 77, 31, 44, 55, 20]
# 新列表为：[17, 20, 26, 31, 44, 54, 55, 77, 93]
assert(bubbleSort([54, 26, 93, 17, 77, 31, 44, 55, 20]) == [17, 20, 26, 31, 44, 54, 55, 77, 93])
思路：泡泡相撞的故事，每次找到一个最大泡泡
1）外循环。从 i = N-1 ~ 2。理解为，本次要发生泡泡碰撞的最远地方，同时记住碰撞完后，最大泡泡就在第 i 位。
2）内循环。从 j = 0 ~ i 。理解位，本次泡泡们，要进行碰撞的地方。
完成一个完整的内循环后，再更换数值。
"""
import numpy as np
import pandas as pd

def swap(a,b):
    a = a^b
    b = a^b
    a = a^b
    return a,b

def bubbleSort(arr):
    if (arr is np.nan or len(arr) < 2 or arr is None) :
        return 
    else:
        arrLen = len(arr)
        for i in range(arrLen - 1,1,-1):
            for j in range(0,i):
                #print('i = {},j = {}'.format(i,j))
                if (arr[j] > arr[j + 1]):
                    arr[j],arr[j+1] = swap(arr[j],arr[j+1])
        return arr
                    
                    
                    
                    
                    
                    
