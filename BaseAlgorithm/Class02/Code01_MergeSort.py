# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:08:29 2019

@author: DELL

归并排序思路
1. 先对函数左边和右边都递归调用 归并排序本身
2. 对处在函数左右之间的数值，进行排序。
默认左右都有序。
2.1 设置辅助列
2.2 数组不越界的情况下，遍历对比左边和右边，当拷贝较小值到辅助列。相等，则拷贝左边列。
2.3 将未遍历完成的剩下的值，拷贝进入辅助队列。
2.4 使用辅助队列的值覆盖掉原有数组

调试心得。把每一层设置FLag，观察
"""

import os
os.chdir(r'D:/Code/github/nowCode/nowCode/BaseAlgorithm/Class02/')
from Utils import * 
import random

def mergSort(L,R,Flag = 'O'):
    mid = int(L + ((R - L)>>1))
    print("Flag = {},arr = {},L = {},mid = {},R = {}".format(Flag,arr[L:R],L,mid,R))
    if(L == R):
        return 
    
    mergSort(L,mid,Flag +'L')
    mergSort(mid + 1 ,R,Flag + 'R')
    merg(L,mid,R,Flag+'M')


def merg(L,mid,R,Flag):
    print('Flag = {},arr = {},L = {},mid = {},R = {}'.format(Flag,arr[L:R],L,mid,R))
    helpArr = []
    p1 = L
    p2 = mid
    while(p1 <= mid - 1 and p2 <= R  -1):
        if(arr[p1] <= arr[p2]):
            helpArr.append(arr[p1])
            p1 = p1 + 1
        else:
            helpArr.append(arr[p2])
            p2 = p2 + 1
    while p1 <= mid - 1:
        helpArr.append(arr[p1])
        p1 = p1 + 1
    while p2 <= R - 1: 
        helpArr.append(arr[p2])
        p2 = p2 + 1
    for i in range(0,len(helpArr)):
        arr[L+i] = helpArr[i]

   
global arr

#testArr = random.sample(range(0,50),4)
#testArr = [10,1,5,8,11,9]
testArr = [17, 49,34, 18]
arr = testArr.copy()

L = 0
R = len(testArr) 
mergSort(L,R)


global num

num = 1

def addFun(n):
    n = n + 1

addFun(num)


















