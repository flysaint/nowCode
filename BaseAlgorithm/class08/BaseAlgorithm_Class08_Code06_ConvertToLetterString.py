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


在位置i，的含义是，将 0~i位置当做一个整体，有多少种可能

"""
import numpy as np

import pandas as pd



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































        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    