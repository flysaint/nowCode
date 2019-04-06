# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:12:22 2019

@author: fly_s
堆排序
1. 数组变成大根堆。每个新插入的数，和它的父节点，对比交换。再循环对比。
2. 大根堆进行排序，将头位置的大数，与尾部数据交换。循环。

"""


def heapSort(arr):
    if arr is None or len(arr) < 2:
        return arr
    # 第一步形成大顶堆
    for i in range(len(arr)):
        heapInsert(arr,i)
    
    # 第二步 1） 交换头位置和尾位置的值。2) 交换后，再次将数组变成大顶堆。3）循环    
    # 先进行一次交换
    # 计算堆的大小。初始 == 数组大小
    lenArr = len(arr)
    lenArr = lenArr - 1
    swap(arr,0,lenArr)
    # 只要堆里还有数据，循环交换
    while(lenArr > 1 ):
        # 将剩余的数组变成大顶堆
        heappify(arr,0,lenArr)
        
        lenArr = lenArr - 1
        
        swap(arr,0,lenArr)


'''
将数组堆化
思路：头部交换来的点，不断跟孩子对比，交换，找到合适的位置，或者没有孩子

循环的边界是 左孩子 < 堆的大小
'''
   
def heappify(arr,index,heapSize):
    
    left = index*2 + 1
    while(left < heapSize):
        
        # 得到左右孩子的最大值
        Largest = left + 1 if (left + 1 < heapSize) and arr[left] < arr[left + 1] else left 
        # 得到孩子和父节点的最大值
        Largest = index if arr[index] > arr[Largest] else Largest
        # 如果 最大值就是父节点，则不需要交换，直接跳出循环
        if Largest == index:
            break
        
        swap(arr,index,Largest)
        # 循环计算
        index = Largest
        left = index*2 + 1
    
 
'''
跟父节点对比。再递归
'''

def heapInsert(arr,index):
    father_index = int((index - 1)/2)
    while(arr[index] > arr[father_index]):
        swap(arr,index,father_index)
        index = father_index
        father_index = int((index - 1)/2)

def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

    
import random

testArr = [1,3,5]

testArr = random.sample(range(100),5)

heapSort(testArr)


















