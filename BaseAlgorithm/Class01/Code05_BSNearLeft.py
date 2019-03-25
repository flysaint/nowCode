# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:15:13 2019
@author: fly_s
题2 在一个有序数组中，找>=某个数最左侧的位置
思路
step1 在左边界 < 右边界的情况下。
step2 获得中间值。
step3 当中间值 >= 查找值。说明找到，但需要继续向左找。记录当前mid，将右边界 = 中间位 - 1，继续向左查找
step4 当中间值 <  查找值。没找到，需要继续向右找。左边界 = 中间位 + 1，继续向右查找
"""
def nearestIndex(arr,value):
    L = 0
    R = arr.length - 1
    index = -1
    while(L < R):
        mid = L + ((R - L) >> 1)
        if(arr[mid] >= value):
            # 记录达标的 mid
            index = mid
            # R 往左缩
            R = mid - 1
        else:
            L = mid + 1
    return index

'''
题3 局部最小值问题
'''
def getLessIndex(arr):
    if(arr is None or len(arr) == 0):
        return -1
    if(len(arr) == 1 || arr[0] < arr[1]):
        return 0
    if (arr[len(arr) - 1] < arr[len(arr) - 2]):
        return len(arr) - 1
    L = 1
    R = len(arr) - 2
    mid = 0
    while(L < R):
        mid = (L + R)/2
        if(arr[mid] > arr[mid - 1]):
            R = mid - 1
        elif(arr[mid] > arr[mid + 1]):
            L = mid + 1
        else:
            return mid
    return L






















