# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:55:23 2019

@author: fly_s

大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
https://blog.csdn.net/qq_35082030/article/details/65450721
https://www.nowcoder.com/questionTerminal/c6c7742f5ba7442aada113136ddea0c3?from=14pdf
"""
def getValueInFib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    numfn1 = 0
    numfn2 = 1
    for i in range(2,n+1):  .
        currentNum = numfn1 + numfn2
        numfn1 = numfn2
        numfn2 = currentNum
    return currentNum



'''
O(logN)解法：由f(n) = f(n-1) + f(n-2)，可以知道
[f(n),f(n-1)] = [f(n-1),f(n-2)] * {[1,1],[1,0]}     
所以最后化简为:[f(n),f(n-1)] = [1,1] * {[1,1],[1,0]}^(n-2)     
所以这里的核心是：     
1.矩阵的乘法     
2.矩阵快速幂（因为如果不用快速幂的算法，时间复杂度也只能达到O(N)）     
    
'''
def Fibonacci(self, n):
        q=[[1,1],[1,0]]
        if n==0: return 0
        res=self.mypower(q,n-1)
        return res[0][0]
    
def mypower(self, a, n):
    ret=[[1,0],[0,1]]
    while n>0:
        if (n&1)==1:
            ret=self.mymultiply(ret, a)
        n>>=1
        a=self.mymultiply(a, a)
    return ret

#Matrix Multiplication
def mymultiply(self, a, b):
    c=[[0 for _ in range(2)] for _ in range(2)]
    for i in range(2):
        for j in range(2):
            c[i][j]=(a[i][0]*b[0][j]+a[i][1]*b[1][j])
    return c


Fibonacci(5)