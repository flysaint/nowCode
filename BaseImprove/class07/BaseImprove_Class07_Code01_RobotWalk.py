# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:17:25 2019

@author: fly_s

题目一
机器人KMP算法达到扩指展定题位目置二方法数
【题目】
假设有排成一行的 N 个位置，记为 1~N，N 一定大于或等于 2。开始时机器人在其中的 M 位
置上(M 一定是 1~N 中的一个)，机器人可以往左走或者往右走，如果机器人来到 1 位置， 那
么下一步只能往右来到 2 位置;如果机器人来到 N 位置，那么下一步只能往左来到 N-1 位置。
规定机器人必须走 K 步，最终能来到 P 位置(P 也一定是 1~N 中的一个)的方法有多少种。给
定四个参数 N、M、K、P，返回方法数。
【举例】
N=5,M=2,K=3,P=3
上面的参数代表所有位置为 1 2 3 4 5。机器人最开始在 2 位置上，必须经过 3 步，最后到
达 3 位置。走的方法只有如下 3 种: 1)从2到1，从1到2，从2到3 2)从2到3，从3到2，从2到3
3)从2到3，从3到4，从4到3
所以返回方法数 3。 N=3,M=1,K=3,P=3
上面的参数代表所有位置为 1 2 3。机器人最开始在 1 位置上，必须经过 3 步，最后到达 3
位置。怎么走也不可能，所以返回方法数 0。

思路，
中止条件，肯定是只剩0步，并且达到P位置，此时 方案+1，否则 0
一般条件，
看在1位置，或者N位置，因为1位置只能到2位置；N位置，只能到N-1位置
其他情况，返回左右两个位置的和
"""



'''
def robitWalk(N,M,K,P):
    ## 中止条件
    if K == 0:
        return 1 if M == P else 0
    # 一般情况
    
    # 如果在1位置
    if M == 1:
        return robitWalk(N,2,K - 1,P)
    elif M == N:
        return robitWalk(N,N-1,K - 1,P)
    else:
        return robitWalk(N,M+1,K-1,P) + robitWalk(N,M-1,K-1,P)
'''  
'''
DP的思路，我有两个可变参数，因此用二维数组存储

'''    
import numpy as np


def robitWalk_DP(N,M,K,P):
    '''
    尝试函数怎么写，动态规划怎么改
    M,K 是两个可变参数
    用二维数组存储。在K==0,M==P，位置是 ==1。K ==0,M!=P，==0。
    K == 1，向上衍生
    
    '''
    # 初始化 0 矩阵
    Walk_Matrix = np.zeros([K+1,N+1])
    
    Walk_Matrix[0][P] = 1
    for i in range(1,K+1):
        for j in range(0,N+1):
            if j == 1:
                Walk_Matrix[i][j] = Walk_Matrix[i-1][2]
            elif j == N:
                Walk_Matrix[i][j] = Walk_Matrix[i-1][N-1]
            else:
                Walk_Matrix[i][j] = Walk_Matrix[i-1][j+1] + Walk_Matrix[i-1][j-1]
                
    return Walk_Matrix[K][M]
                
                
                
                
    
    
    
    
    
    



'''

def robitWalk_DP(N,M,K,P):
    arr = np.zeros([M+1,K+1])
    
    arr[P][0] == 1
    for j in range(1,K+1):
        for i in range(1,N+1):
            if i == 1:
                arr[i][j] = arr[i+1][j-1]
            elif i == N:
                arr[i][j] = arr[i-1][j-1]
            else:
                arr[i][j] = arr[i+1][j-1] + arr[i-1][j-1]
    return arr[M][K]
'''

if __name__ == '__main__':
    
    print(robitWalk(N=5,M=2,K=3,P=3)   )
    print(robitWalk_DP(N=5,M=2,K=3,P=3))
    















    
    
    
    
    