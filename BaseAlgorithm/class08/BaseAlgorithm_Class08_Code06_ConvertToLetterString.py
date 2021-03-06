# -*- coding: utf-8 -*-
"""
Created on Sun May 26 22:44:35 2019

@author: fly_s

BaseAlgorithm_Class08_Code06_ConvertToLetterString
题目六
规定1和A对应、2和B对应、3和C对应...
那么一个数字字符串比如"111"，就可以转化为"AAA"、"KA"和"AK"。
给定一个只有数字字符组成的字符串str，返回有多少种转化结果。

思路：
在每一个位置，从开始，到中间，到最后，考虑能够达到它们的路径，和它们能达到的路径。


从每个位置出发，看每个位置能返回的转化结果
因为字母总共只有26位，因此最多只能看两位

步骤：
1. 外层函数。转化成 内部可以调用的
2. 内层函数。考虑三种情况，进行统计
1) 特殊情况。字符串程度 == 0，说明只有1种情况。
2) 当前位置 == 0 。没有可以转换对象。返回0
3) 当前位置 == 1 。考虑切割1，和切割1和1后面1位的情况。
4) 当前位置 == 2 。考虑切割2，和切割2和2后面1位的情况


在位置i，的含义是，将 0~i位置当做一个整体，再加上后面的可能，共有多少种可能


终止位置理解.
前面的我不管，从i出发，有多少种可能。
i之前的位置，如何转化已经做过决定了，不用关心。
终止位置，
两种理解。
1）来到最后位置，不管前面，但前面已经做了决定，这个决定就是一种可能。
2）来到最后位置，只有空字符串了，空字符串也是1种可能。
疑问：前面的一定可以做转换吗？可以
"""
import numpy as np

import pandas as pd

def process(arr,i):
    
    
    # 中止条件
    # 达到最后
    if i == len(arr):
        return 1
    
    if arr[i] == 0:
        return 0
    
    if arr[i] == '1':
        count = process(arr,i+1)
        if i + 1 < len(arr):
            count += process(arr,i+2)
        return count 
       
    if arr[i] == '2':
        count = process(arr,i+1)
        if i + 1 < len(arr) and 0<= arr[i+1] <= 6:
            count += process(arr,i+2)
        return count
    
    return process(arr,i+1)
    
def get_count_dp(arr):
    
    count_list = np.zeros(len(arr)+1)
    # 终止位置
    count_list[len(arr)] = 1
    
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == '1':
            count_list[i] = count_list[i+1]
            if i + 1 < len(arr):
                count_list[i] += count_list[i+2]
                
        elif arr[i] == '2':
            count_list[i] = count_list[i+1]
            if i + 1 < len(arr) and 0 <= arr[i+1] <= 6:
                count_list[i] += count_list[i+2]
        else:
            count_list[i] = count_list[i+1]
    return count_list[0]
        
            
    
    
    
    
    
    
    

if __name__ == '__main__':
    testStr = '111'
    
    #count_list = np.zeros(len(testStr))
    #print(process(testStr,0))
    print(get_count_dp(testStr))



























def get_count_DP(testStr):
    
    # 建立动态规划矩阵
    count_list = list(np.zeros(len(testStr)+1))

    # 边界条件
    count_list[len(testStr)] = 1
    
    for i in range(len(testStr) - 1,-1,-1):
        if testStr[i] == '0':
            count_list[i] = 0
        elif testStr[i] == '1':
            count_list[i] = count_list[i+1]
            if len(testStr)  > i + 1:
                count_list[i] += count_list[i+2]
        elif testStr[i] == '2':
            count_list[i] = count_list[i+1]
            if len(testStr)  > i + 1 and int(testStr[i+1]) <= 6:
                count_list[i] += count_list[i+2]
        else:
            count_list[i] = count_list[i+1]
    
    return count_list[0]


def get_count_Inner(testStr,i):
    
    if(len(testStr) == i):
        return 1
    
    if(testStr[i] == '0'):
        return 0
    
    if(testStr[i] == '1'):
        res = get_count_Inner(testStr,i+1)
        
        if len(testStr) > i+1:
            res += get_count_Inner(testStr,i+2)
        return res
        
    if(testStr[i] == '2'):
        
        res = get_count_Inner(testStr,i+1)
        
        if len(testStr) > i+1 and int(testStr[i+1]) <= 6:
            res += get_count_Inner(testStr,i+2)
        return res
    
    # testStr[i] = 3~9，则和下一位i+1相同
    return get_count_Inner(testStr,i+1)
        

if __name__ == '__main__':
    testStr = '11111'
    print(get_count_Inner(testStr,0))
    print(get_count_DP(testStr))































        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    