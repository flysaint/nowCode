# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 23:59:39 2019

@author: fly_s
快速排序
思路：要用到partion
遍历数组。已知数组。当前下标，小于区域，大于区域。
初始状态。小于区域 less 等于 当前下标的前一位 l-1。 大于区域 more 等于 数组的前一位。当前下标
规则：
1）当前值 == 划分值。当前值下标移动一位。
2）当前值 < 划分值。当前值与小于区域后面一位交换，当前值向后移动一位。小于区域向右移动一位。
3）当前值 > 划分值。当前值 与 大于区域前面一位交换，当前值不变。大区域向左增加一位。

"""
import random

def quickSort(arr):
    if arr is None or len(arr) < 2:
        return
    quickSort_process(arr,0,len(arr) - 1)

def quickSort_process(arr,l,r):
    if l < r:
        swap(arr,l + random.sample(range(1,r - l + 1,1),1)[0],r)
        p = partion(arr,l,r)
        quickSort_process(arr,l,p[0] - 1)
        quickSort_process(arr,p[1] + 1,r)


def partition(arr,l,r):
    '''
    我的问题：
    1. 需要几个指针？起点怎么设置？
    使用 l 做指针，因为less区域后面还有等于区域
    使用 more 做指针，因为  r 不能动，因为一直要做对比
    
    起点怎么设置？
    
    less 设置 l - 1，因为 l 位置还没有 划到 less 区域里面
    more 设置 r ，因为 r 位置也没有划到 more 区域里面
    
    2. 怎么进行循环对比？谁跟谁比？ 比完后怎么交换？为什么这么交换？
    一句话总结。
    肯定是 指针位置 l 和 r 做对比。
    大于。交换l和 more -1 (大于区域的前一位)，这样大于区域可以向左一位。但保持l不变，因为交换的值还要做对比。
    等于。l直接后移动一位。因为起始值，l就在more的后一位。能保证等于区域在小于区域后面。
    小于。l与 less + 1(小于区域后一位)交换，less + 1,l + 1。等于 把当前值交换到 小于区域下一位，同时扩大小于区域。指针后移。
    
    
    总结：Partition的故事。对人进行排序。
    1. 故事的背景。来了一些人。我们只认识两个，名字分别叫 ，最左边的叫 阿左，右边的叫阿右。
    2. 故事的目标。要按照 小右的身高，将这些人分开。分成 小，等，大三个组。
    3. 故事的帮手。为了分组，于是请了两个人帮忙。一个叫 阿小，一个阿大。分别用来记录 小组和大组的 边界。
    4. 故事的开始。阿左站在最左边，阿小站在阿左的左边。因为目前小组没人， 阿右站在最右边，阿大和阿右站在一起。因为目前大组没人，而阿右是裁判，不算大组的人
    5. 故事的停止条件。什么时候，所有人对比完成，当阿左碰上阿大。因为阿小在阿左的左边，阿右不能动。
    6. 故事的叙述。阿右是裁判，阿左每次做对比，大于，要换，more动，我不动。等于，不换，我要动起来。小于 要换，less动，我也动。
    7. 故事的结尾。返回阿小和阿右。
    '''
                                                        
    less = l - 1
    more = r
    while(l < more):
        if arr[l] > arr[r]:
            # 要把 大值 交换到 大于区域
            swap(arr,l,more-1)
            # 大值指针，要移动一位
            more -= 1
        elif arr[l] == arr[r]:
            #swap(arr,l,less+1)
            l += 1
        elif arr[l] < arr[r]:
            # less 要么等于 l -1。要么等于 l - i，所以一定是对比过的值。
            # less + 1 要么就是 l 自己，自己和自己交换，没有任何风险。
            # less + 1，要么是 等于区域的值，因为 l 经过的地方，都是等于区域。交换后，等于区域会继续保持在小于区域的后面
            swap(arr,l,less+1)
            l += 1
            less += 1
    swap(arr,l,r)
    return less,more
            
    
'''
partion过程怎么和快速排序结合

我的工具，每次回让partition等于区域两边的区域,小于区域，相对大于区域是有序的。
那就和归并排序类似。只要不断递归就可以。
每次随机从 l,r之间选择一个位置，进行交换。中止条件，肯定是相等相关的.

中止条件，左边界 碰到 右边界。
Patition返回小于区域和大于区域的边界。两边再分别排序。

'''


def QuickSort(arr,l,r):
    
    if(l >= r):
        return 
    
    m = l + random.sample(range(0,r-l+1),1)[0]
    # 将这个数 交换到 末尾
    swap(arr,m,r)
    q,p = partition(arr,l,r)
    QuickSort(arr,l,q)
    QuickSort(arr,p,r)

        

def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


import random
import operator
import copy

testArr1 = random.sample(range(100),10)
testArr2 = copy.copy(testArr1)

for i in range(0,100):
    QuickSort(testArr1,0,len(testArr1)-1)
    if not (operator.eq(testArr1,sorted(testArr2))):
        print('bad')
        print(testArr1)
        break
    
    
    










    
    




















