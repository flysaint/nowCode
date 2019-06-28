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


def partion(arr,l,r):
    # 小于区域为空
    less = l - 1
    # 大于区域为空
    more = r
    while(l < more):
        if arr[l] == arr[r]:
            l = l + 1
        elif arr[l] < arr[r]:
            # 为什么要交换？ 因为小于区域右一位，可能是等于值
            swap(arr,less+1,l)
            less = less + 1
            l = l + 1
        else:
            swap(arr,more-1,l)
            more = more - 1
    # 交换划分值到中间位置
    swap(arr,more,r)
    # 返回相等区域的值
    return less + 1,more


def partion(arr,l,r):
    '''
    将数组的左右两边都变的有序
    假设已经是有序的了，再对左右两边递归继续partion
    所以我要分几部分进行操作？
    
    肯定需要随机，在左边，右边，进行Partion
    
    我的问题：
    1. 怎么实现小中大三个区域？ 需要几个额外的指针？
    我用两个指针分别代表大小区域可以吗？ 用两个数替代，但他们代表的不是指针，而是小于区域右边界，和大于区域的左边界。
    注意小于区域，只有右边界。且是包含关系。大于区域，只有左边界，且是包含关系。
    但是将 输入参数 l，当做左指针。将大于区域的左边界，当做右指针。
    
    小区域的指针是怎么移动？怎么交换的？我现在感觉小于区域和等于区域都不用交换。
    相等的时候，确实不用交换。直接移动指针。
    小于的时候，要进行交换，
    大于区域的指针是怎么赋值的？我感觉应该设置到右边界 - 1的位置，这样就等于和 右边界前一位进行对比和交换。
    
    '''
    if l >= r:
        return 
    # 需要两个指针
    P1 = l - 1
    P2 = r - 1
    while(P1 < P2):
        # 小于区域
        if arr[P1] < arr[r]:
            P1 += 1
        # 等于区域
        elif arr[P1] == arr[r]:
            P1 += 1
        # 大于区域
        else:
            swap(arr,P1,r)













def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

testArr = [1,5,6,3]
testArr = random.sample(range(100),10)

equalArr = partion(testArr,0,3)

import operator

testArr1 = random.sample(range(0,100),50)
testArr2 = testArr1.copy()

for i in range(0,100):
    quickSort(testArr1)
    if not (operator.eq(testArr1,sorted(testArr2))):
        print('bad')
        print(testArr1)
        break










    
    




















