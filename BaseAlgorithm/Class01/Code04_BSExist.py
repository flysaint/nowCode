# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 21:15:28 2019
@author: fly_s
二分法
"""
'''
第1题 在一个有序数组中，找某个数是否存在
思考：用二分的方式求解
step1 在左边界 < 右边界的情况。
step2 获得当前中间位的数值
step3 
如果 找到，则返回；
如果 值 > 中间值，则从 中间位右一位，向右开始查看
如果 值 < 中间值，则从 中间位左一位，向左开始查看
'''
def BSexist(arr,num):
    if (sortedArr is np.nan or sortedArr is None or len(sortedArr) == 0):
        return False
    L = 0
    R = len(arr)-1
    while(L < R):
        # mid = (L + R)/2 在下标很大时，可能溢出，比如超过了整型的范围. 
        # (L+R)/2 == L + (R - L)/2 == L + ((R - L) >> 1 右移一位。位运算更快，要保证时正数
        # >> 右移一位，最高位（符号位）补。比如最高位是1，右移一位，最高位是两个1。记得 负数的二进制是 原码->反码->补码
        # >>> 右移一位，不管符号位，用0来补
        mid = L + ((R - L) >> 1) 
        print('L = {},mid = {},R = {}'.format(L,mid,R))
        print('arr[min] = {},arr[mid] = {},arr[max] = {}'.format(arr[L],arr[mid],arr[R]))
        if num == arr[mid]:
            return True
        elif num > arr[mid]:
            L = mid + 1
        else:
            R = mid - 1
    return arr[L] == num

arrSorted = [17, 20, 26, 31, 44, 54, 55, 77, 93]
BSexist(arrSorted,93)















