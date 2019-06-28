# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 10:54:00 2019

@author: fly_s


BaseImprove_Class07_Code02_CoinsMin
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

arr = [5,2,3]

sorted(arr,reverse = True)

# 到了i位置，使用i位置的牌，能否把rest的金额分完
def process(arr,i,rest):
    
    sorted(arr,reverse = True)
    # 边界条件
    # 到了最后的位置，并且把钱分完了
    if i == len(arr):
        return 0 if rest == 0 else -1
    
    # 考虑是第一次的情况
    res = -1
    
    # 一般情况
    # 本位置上的牌用多少张
    k = 0
    while arr[i]*k <= rest:
        # 使用 本位置k张牌
        next_rest = process(arr,i+1,rest - k*arr[i])
        # 是否使用本轮的方案
        if next_rest != -1:
            res = next_rest + k if res == -1 else min(res,next_rest+k)
        k += 1
    return res
            
        
        
    
    
    
    
    
    
    
    



'''
def process(arr,i,rest):
    # 中止条件
    # 当用完所有的 数组数据后，还有多少钱要分
    if i == len(arr):
        # 钱能分为，返回0，不能返回 -1
        return 0 if rest == 0 else -1
    
    # 最少张数，初始时为-1，因为还没找到有效解
    res = -1
    
    # 一般情况
    # 依次使用每个位置上的数据后
    k = 0
    # 仅使用当前的面值
    while k * arr[i] <= rest :
        # 当前位，使用k个arr[i]，共需要多少张牌
        n_rest = process(arr,i+1,rest - k * arr[i])
        # 需要的牌不是 -1 张，说明 本轮 方案可行
        if n_rest != -1:
            # 是 res == -1，说明是第一次分配吗？
            # 不是 -1,说明已经找到了方案，看历史方案，和当前新的方案，哪种更优？
            res = n_rest + k if res == -1 else min(res,n_rest + k)
        
        k += 1
    return res
      

'''


if __name__ == '__main__':
    arr=[5,2,3]
    aim=20
    
    print(process(arr,0,aim))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    