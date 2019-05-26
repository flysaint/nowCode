# -*- coding: utf-8 -*-
"""
Created on Sun May 26 18:07:33 2019

@author: fly_s

一个数据流中，随时可以取得中位数

当选择的样本，产生了新的样本，样本重新加入计算，使用堆，比如哈夫曼编码；如果不能，则排序

思路
准备 两个堆，一个是大根堆，一个是小根堆。
1. 第一个数。进大根堆。
1. 非第一个新出现的数。 <= 大根堆的堆顶，则进大根堆；否则就进小根堆
2. 检查差值。如果两个堆的大小，差值> 2，则调整。从较多那个堆，拿出堆顶，放到另外一个堆。

永远较小的 n/2个在大根堆里；较大的n/2个，在小根堆里。
size 不一样时，较大的堆的堆顶，就是中位数；size一样，两个堆的堆顶 相加 /2 就是中位数。

"""



import heapq
 
class BigHeap():
    def __init__(self):
        self.arr = list()
    def heap_insert(self, val):
        heapq.heappush(self.arr, -val)
    def heapify(self):
        heapq.heapify(self.arr)
    def heap_pop(self):
        return -heapq.heappop(self.arr)
    def get_top(self):
        if not self.arr:
            return
        return -self.arr[0]
    
 
class SmallHeap():
    def __init__(self):
        self.arr = list()
    def heap_insert(self, val):
        heapq.heappush(self.arr, val)
    def heapify(self):
        heapq.heapify(self.arr)
    def heap_pop(self):
        return heapq.heappop(self.arr)
    def get_top(self):
        if not self.arr:
            return
        return self.arr[0]
    
    
class MedianHolder():
 
    def __init__(self):
        self.bigHeap = BigHeap()
        self.smallHeap = SmallHeap()
 
    def addNum(self, num):
        if len(self.bigHeap.arr) == 0:
            self.bigHeap.heap_insert(num)
            return
        if self.bigHeap.get_top() >= num:
            self.bigHeap.heap_insert(num)
        else:
            if len(self.smallHeap.arr) == 0:
                self.smallHeap.heap_insert(num)
                return
            if self.smallHeap.get_top() > num:
                self.bigHeap.heap_insert(num)
            else:
                self.smallHeap.heap_insert(num)
        self.modifyTwoHeapSize()
 
    def getMedian(self):
        smallHeapSize = len(self.smallHeap.arr)
        bigHeapSize = len(self.bigHeap.arr)
        if smallHeapSize + bigHeapSize == 0:
            return None
        smallHeapHead = self.smallHeap.get_top()
        bigHeapHead = self.bigHeap.get_top()
        if (smallHeapSize + bigHeapSize) %2 == 0:
            return (smallHeapHead+bigHeapHead)/2
        else:
            return smallHeapHead if smallHeapSize > bigHeapSize else bigHeapHead
 
    def modifyTwoHeapSize(self):
        smallHeapSize = len(self.smallHeap.arr)
        bigHeapSize = len(self.bigHeap.arr)
        if smallHeapSize == bigHeapSize + 2:
            self.bigHeap.heap_insert(self.smallHeap.heap_pop())
        if bigHeapSize == smallHeapSize + 2:
            self.smallHeap.heap_insert(self.bigHeap.heap_pop())
            
            
            
if __name__ == '__main__':
    arr = [68,51,42,92,13,46,24,58,62,72,32]
    medianHold = MedianHolder()
    for i in range(len(arr)):
        medianHold.addNum(arr[i])
        print(medianHold.getMedian())        
        
            
            
        
            
            
            
    