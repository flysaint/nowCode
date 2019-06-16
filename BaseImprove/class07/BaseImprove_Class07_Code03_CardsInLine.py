# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:21:39 2019

@author: fly_s

题目三
排成一条线的纸牌博弈问题
【题目】
给定一个整型数组 arr，代表数值不同的纸牌排成一条线。玩家 A 和玩家 B 依次拿走每张纸 牌，
规定玩家 A 先拿，玩家 B 后拿，但是每个玩家每次只能拿走最左或最右的纸牌，玩家 A 和 玩
家 B 都绝顶聪明。请返回最后获胜者的分数。
【举例】
arr=[1,2,100,4]。
开始时，玩家 A 只能拿走 1 或 4。如果玩家 A 拿走 1，则排列变为[2,100,4]，接下来玩家 B
可以拿走 2 或 4，然后继续轮到玩家 A。如果开始时玩家 A 拿走 4，则排列变为[1,2,100]，接
下 来玩家 B 可以拿走 1 或 100，然后继续轮到玩家 A。玩家 A 作为绝顶聪明的人不会先拿 4，
因为 拿 4 之后，玩家 B 将拿走 100。所以玩家 A 会先拿 1，让排列变为[2,100,4]，接下来玩
家 B 不管 怎么选，100 都会被玩家 A 拿走。玩家 A 会获胜，分数为 101。所以返回 101。
arr=[1,100,2]。
开始时，玩家 A 不管拿 1 还是 2，玩家 B 作为绝顶聪明的人，都会把 100 拿走。玩家 B 会
获胜，分数为 100。所以返回 100。

思路：常规试法，一个数组在L->R范围上怎么拿？在每个位置上，有还是没有，拿还是不拿，比如背包问题。
拿还是不拿，两个分支。都去试验。

先找Basecase，就是终止条件。可以想到，要将方案分为先手和后手。
假设现在是左边位置是L，右边位置是R。

先手f(L,R)：
Basecase（终止条件）。只剩最后一张牌，此时 L == R。只能选择这一张牌。arr[R]
一般情况。选择L位置，或者R位置，具体选择哪个位置，看选择后，加上之后的后手，最大值是多少？
f(L,R) = max(arr[L] + s(L+1,R),arr[R] + s(L,R-1)

后手s(L,R)
Basecase(终止条件)。只剩下最后一张牌，此时 L == R。此时牌会被先手选走，s(L,R) == 0
一般情况。选择L位置，或者选择R位置，看选择后，下一轮对方是先手，。
s(L,R) = min(f(L+1,R),f(L,R-1))

注意。都是从自己的角度出发，s(L+1,R)，就是当在L+1,R范围上，我又是后手怎么处理？

"""
def win(arr):
    if arr is None or len(arr) == 0:
        return 0
    L = 0
    R = len(arr) - 1
    return max(f(arr,L,R),s(arr,L,R))

# 先手
def f(arr,L,R):
    if (L == R):
        return arr[L]
    
    return max(arr[L] + s(arr,L+1,R),arr[R] + s(arr,L,R-1))

# 后手
def s(arr,L,R):
    if (L == R):
        return 0
    
    return min(f(arr,L+1,R),f(arr,L,R-1))
'''
进行动态规划
核心是通过数组表示 两组递归的结果

是对角线元素不断填充的过程
步骤：
1. baseCase填写。
f数组。L = R的时候，返回arr[L]
'''
import numpy as np

def dp(arr):
    
    # 构建基础矩阵
    L = 0
    R = len(arr) - 1
    f = np.zeros([len(arr),len(arr)])
    s = np.zeros([len(arr),len(arr)])
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                f[i][j] = arr[i]
                s[i][j] = 0
            else:
                f[i][j] = 0
                
                
    # 循环赋值。对两个矩阵，循环遍历对角线
    row = 0
    col = 1
    while(col < len(arr)):
        i = row
        j = col
        while(i < len(arr) and j < len(arr)):
            f[i][j] = max(arr[i] + s[i+1][j],arr[j]+s[i][j-1])
            s[i][j] = min(f[i+1][j],f[i][j-1])
            i += 1
            j += 1
        
        col += 1    
   
    return max(f[0][col-1],s[0,col-1])         
            
            
            
            
            
            
    
    


if __name__ == '__main__':

    testArr = [1,2,100,4]
    print(dp(testArr))
    #print(win(testArr))
    
































