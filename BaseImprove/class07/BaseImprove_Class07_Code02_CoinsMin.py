# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 10:54:00 2019

@author: fly_s

题目二
换钱的最少货币数
【题目】
给定数组 arr，arr 中所有的值都为正数且不重复。每个值代表一种面值的货币，每种面值
的货币可以使用任意张，再给定一个整数 aim，代表要找的钱数，求组成 aim 的最少货币
数。
【举例】
arr=[5,2,3]，aim=20。
4 张 5 元可以组成 20 元，其他的找钱方案都要使用更多张的货币，所以返回 4。
arr=[5,2,3]，aim=0。
不用任何货币就可以组成 0 元，返回 0。
arr=[3,5]，aim=2。
根本无法组成 2 元，钱不能找开的情况下默认返回-1。

"""

def minCoins1(arr,aim):
    

def process(arr,aim):
    '''
    将所有单个单词组成的可能，放入数组。
    遍历数组每一个值，求出里面的最小值
    '''
    max_nums = []
    for index in range(len(arr)):
        max_nums.append(int(aim/arr[index]) + 1)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    