# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 10:32:36 2019

@author: fly_s
堆排序
1. 插入。将数组依此插入，并形成大顶堆。
将数组看成完全二叉树，插入的节点 > 父节点,则交换。一直到越界
2. 排序。将顶部取出，放到末尾。heapsize - 1。等于末尾的值就是最大值。
循环，直到整个数组全部取出。

注意：在函数中，对传入的数组进行操作，操作会被保留，如交换，赋值等
"""
import random

testArr = random.sample(range(0,100),5)

def heapSort(arr):
    if arr is None or len(arr) < 2:
        return arr
    for i in range(0,len(arr)):
        heapInsert(arr,i)
    
    lenArr = len(arr)
    lenArr = lenArr - 1
    swap(arr,0,lenArr)
    
    while(lenArr > 0):
        heapify(arr,0,lenArr)
        lenArr = lenArr - 1
        swap(arr,0,lenArr)

'''
功能：递归和父节点对比，大于，则交换
步骤：
1. while 判断当前位置值 ，是否大于 父节点值。
2. 满足，则交换位置
3. 标记变成父节点。
'''
def heapInsert(arr,index):
    # 也照顾到了0位置，因为 (0 - 1)/2 == 0
    while(arr[index] > arr[int((index - 1)/2)]):
        swap(arr,index,int((index - 1)/2))
        index = int((index - 1)/2)

'''
功能：经过上次，大根堆顶部和末尾交换后。当前数组，肯定不是大根堆。
0位置的值，需要调整，重新变成大根堆。
思路
1. 跟左右孩子对比。跟较大值交换
2. 更新父节点位置，继续对比。 
步骤：
1. 获取的左孩子位置。
2. 当左孩子位置没有越界
3. 对比左右孩子，获得较大值。
4. 较大值跟本轮父节点对比，标记较大值。
5. 如果父节点是大值，则不需要进行交换。直接跳出
6. 交换大值和本轮父节点
7. 更新父节点。

'''
def heapify(arr,index,size):
    left = int(index * 2 + 1) # 左孩子的下标
    while(left < size):# 未越界的情况下
        # 存在右孩子，且右孩子更大；否则，使用左孩子做下标
        largeIndex = left + 1 if (left + 1 < size) and arr[left + 1] > arr[left]  else left 
        largeIndex = index if arr[index] > arr[largeIndex] else largeIndex
        if largeIndex == index:
            break
        swap(arr,index,largeIndex)
        
        index = largeIndex
        left = int(index * 2 + 1)
        

def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
testArr = [1,5,3]
         

heapSort(testArr)

    





























