# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 09:22:31 2019

@author: DELL

堆排序

1. 先将数组生成大根堆
2. 再将大根堆，堆头位置的数，移到堆尾，再让剩余数字保持大根堆的形态

步骤
1. 数组依次插入成大根堆
2. 堆顶数据依次出栈，再将剩余的变成大根堆

"""


def heapSort(arr):
    if arr is None or len(arr) < 2:
        return arr
    lenArr = len(arr)
    for i in range(1,lenArr):
        insertHeap(arr,i)
        
    # 将堆首位置不断和队尾交换，再保留原队列顺序
    heapSize = lenArr
    swap(arr,0,heapSize - 1)
    heapSize = heapSize - 1
    
    while(heapSize > 0):
        heapFy(arr,heapSize)      
        swap(arr,0,heapSize - 1)
        heapSize = heapSize - 1
        

def insertHeap(arr,i):
    '''
    不停和爹做对比，大于爹，则交换；在递归对比
    '''
    while(arr[i] > arr[int((i - 1) / 2)]):
        swap(arr,i,int((i - 1)/2))
        i = int((i - 1)/2)

def heapFy(arr,i,heapSize):
    # 和左右孩子做对比
        left = 2 * i + 1
        right = 2 * i + 2
        while( i < heapSize):
            large_Index = right if right < heapSize - 1 and arr[right] > arr[left] else left
            large_Index = i if arr[i] > arr[large_Index] else large_Index
            swap(arr,large_Index,i)
            i = large_Index
            


            
def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
            
testArr = [5,1,6]

heapSort(testArr) 
    
heapFy(testArr,0,2)
    








    



