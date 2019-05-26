# -*- coding: utf-8 -*-
"""
Created on Sat May 25 23:29:20 2019

@author: fly_s

一块金条切成两半，是需要花费和长度数值一样的铜板的。比如长度为20的金
条，不管切成长度多大的两半，都要花费20个铜板。
一群人想整分整块金条，怎么分最省铜板?
例如,给定数组{10,20,30}，代表一共三个人，整块金条长度为10+20+30=60。
金条要分成10,20,30三个部分。 如果先把长度60的金条分成10和50，花费60；
再把长度50的金条分成20和30，花费50；一共花费110铜板。
但是如果先把长度60的金条分成30和30，花费60；再把长度30金条分成10和20，
花费30；一共花费90铜板。
输入一个数组，返回分割的最小代价。
思路：
每次选择两个最小的数值，形成小根堆。这是哈夫曼编码问题
哈夫曼编码处理的问题
1. 和原始顺序无关。
2. 两个共同共同的指标。两个指标累加或累乘一个指标。

步骤：
1. 小顶堆插入数据。通过 PriorityQueue 实现。
2. 每一轮取出两个最小数据，累加，将和插入 PriorityQueue队列。
3. 递归执行，直到数组中已经没有元素。

"""

import threading
import time
import queue

   
pQ = queue.PriorityQueue()

pQ.put(1)

print(pQ.qsize() )
pQ.get()
print(pQ.qsize())

def lessMoney(arr):
    
    pQ = queue.PriorityQueue()
    
    for i in range(len(arr)):
        pQ.put(arr[i])
    
    while(pQ.qsize() > 1):
        
        sum_num = 0
        cur_num = 0
        
        record_num = cur_num = pQ.get()
        cur_num = cur_num + pQ.get()
        
        sum_num = sum_num + cur_num
        print("num1 = {},num2 = {},sum_num = {}".format(record_num,cur_num,sum_num))
        pQ.put(cur_num)
    
    return sum_num

if __name__ == "main":
    
    testArr1 = [6,7,8,9]
    
    testArr2 = [7,5,3,2,1,6,7]
    
    final_num = lessMoney(testArr2)
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    





































































































