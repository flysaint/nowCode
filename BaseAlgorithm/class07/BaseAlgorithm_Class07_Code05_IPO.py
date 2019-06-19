# -*- coding: utf-8 -*-
"""

Created on Sun May 26 16:16:29 2019
@author: fly_s
BaseAlgorithm_Class07_Code05_IPO
输入：
正数数组costs
正数数组profits
正数k
正数m
含义：
costs[i]表示i号项目的花费
profits[i]表示i号项目在扣除花费之后还能挣到的钱(利润)
k表示你只能串行的最多做k个项目
m表示你初始的资金
说明：
你每做完一个项目，马上获得的收益，可以支持你去做下一个项目。
输出：
你最后获得的最大钱数。
testexample

k=2, W=0, Profits=[1,2,3], Capital=[0,1,1]
"""


k=2
W=0
Profits=[1,2,3]
Capital=[0,1,1]

def findMaxValue(k,W,Profits,Capital):

    Projects = []
    
    for i in range(len(Profits)):
        
        Projects.append([Profits[i],Capital[i]])
    
    sorted(Projects)
    i = len(Projects) - 1
    while( k > 0 and i >= 0):
        
        if(Projects[i][1] > W):
            i -= 1
        else:
            
            W += Projects[i][0]
            k -= 1
            Projects.pop(i)
            
            i = len(Projects) - 1
            
            



def findMaximizedCapital( k, W, Profits, Capital):
    #将利润和资本通过zip函数，转化成1对1的列表
    num=[x for x in zip(Profits,Capital)]
    #将利润从小到大排序
    num.sort()
    while k and num:
        #利用条件从利润最大的条件往前选，把项目资本大于当前资本W的，踢出去，选择满足条件的。
        i = len(num) - 1
        while i >= 0 and num[i][1] > W:
            i -= 1
        #如果只剩下第一个，则终止循环
        if i < 0:
            break
        W += num[i][0]
        num.pop(i)
        k -= 1
    return W



findMaximizedCapital(k=2, W=0, Profits=[1,2,3], Capital=[0,1,1])














