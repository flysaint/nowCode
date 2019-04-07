# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:18:43 2019

@author: fly_s

问题：反转字符串
思考：
分为3个部分
1. 定义Node数据类型。主要是对象有下个值
2. 定义形成链表的函数。
3. 定义链表反转的函数。

"""

class Node:
    def __init__(self,element,_next = None):
        self.element = element
        self.next_node = _next
        
        
def insertNode(pHead,i):
    '''
    将新数据插入节点
    '''    
    node = Node(i)
    if pHead == None:
        pHead = node
    else:
        p = pHead
        while(p.next_node):
            p = p.next_node
        
        p.next_node = node
    return pHead


def reveseList(pHead):
    '''
    思路：创建另一辅助list，将输入传入。再反响传出。
    
    '''
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    
    #testNode = Node(1)
    testNode = None
    for i in range(10):
        testNode = insertNode(testNode,i)
    p = testNode
    while p:
        print(p.element,end = " ")
        p = p.next_node
        




