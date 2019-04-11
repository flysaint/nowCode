# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:53:07 2019

@author: DELL
题目：
求数组左侧的小和。案例[1,3,5]
则
1是3，和5的小值。+ 2
3是5的小值。+ 3
5没有小值。+0，
最终等于5
和归并排序的联系与区别
联系
1.正好通过归并排序实现。细分到每个叶子上，相邻的值都进行了一次对比。可以得到相邻值的小值。
2.排序完成后，非叶子树节点上，左侧可以和右侧对比。得到左侧每个值，相比于整个右侧的小值。
区别
1. 当左值右值相等时。优先拷贝右值，因为此时右值有多少相等的值，尚未确认。
2. 只有对比时，才产生小值。想象整棵树。

"""

import random

def mergSortLitSum(lst):
    if len(lst) == 1:
        return 0,lst
    m = int(len(lst)/2)
    
    lSum,L_lst = mergSortLitSum(lst[:m])
    rSum,R_lst = mergSortLitSum(lst[m:])
    
    mergSumNum,sortedLst = mergSum(L_lst,R_lst)
    return (lSum + rSum + mergSumNum),sortedLst

def mergSum(L_lst,R_lst):
    helpArr = []
    p1 = 0
    p2 = 0
    mergSumNum = 0
    while(p1 < len(L_lst) and p2 < len(R_lst)):
        if (L_lst[p1] < R_lst[p2]):
            mergSumNum = mergSumNum + (len(R_lst) - p2)*L_lst[p1]
            helpArr.append(L_lst[p1])
            p1 = p1 + 1
        else:
            helpArr.append(R_lst[p2])
            p2 = p2 + 1
    
    while(p1 < len(L_lst)):
        helpArr.append(L_lst[p1])
        p1 = p1 + 1
    
    while(p2 < len(R_lst)):
        helpArr.append(R_lst[p2])
        p2 = p2 + 1
    
    return   mergSumNum,helpArr  
    



testArr = [1,5,3,2,8]

testArr = random.sample(range(0,100),10)

num,arrSorted = mergSortLitSum(testArr)



'''
逆序对
'''


def mergSortCompare(lst):
    if len(lst) == 1:
        return [],lst
    m = int(len(lst)/2)
    
    L_Compare,L_lst = mergSortCompare(lst[:m])
    R_Compare,R_lst = mergSortCompare(lst[m:])
    
    M_Compare,sortedLst = mergCompare(L_lst,R_lst)
    return (L_Compare + R_Compare + M_Compare),sortedLst

def mergCompare(L_lst,R_lst):
    helpArr = []
    p1 = 0
    p2 = 0
    M_Compare = []
    while(p1 < len(L_lst) and p2 < len(R_lst)):
        if (L_lst[p1] <= R_lst[p2]):
            helpArr.append(L_lst[p1])
            p1 = p1 + 1
        else:
            M_Compare.append({L_lst[p1]:R_lst[p2]})
            helpArr.append(R_lst[p2])
            p2 = p2 + 1
    
    while(p1 < len(L_lst)):
        helpArr.append(L_lst[p1])
        p1 = p1 + 1
    
    while(p2 < len(R_lst)):
        helpArr.append(R_lst[p2])
        p2 = p2 + 1
    
    return   M_Compare,helpArr  
    
    
    
testArr = [1,5,3,2,8]

    
revese_list,sortedLst = mergSortCompare(testArr)
