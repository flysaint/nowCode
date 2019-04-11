# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:01:31 2019

@author: fly_s
"""
# https://blog.csdn.net/The__Apollo/article/details/78769400
# 方法一：利用三个指针逐个翻转
def func1(head):
    p = head
    q = head.next
    p.next = None
    while q:
        r = q.next
        q.next = p
        p = q
        q = r
    return p 

# 方法二：尾插法翻转
def func2(head):
    p = head.next
    while p.next:
        q = p.next
        p.next = q.next
        head.next = q
        q.next = p

    p.next = head
    head = head.next
    p.next.next = None
    return head

# 递归
    
def func3(head):
    if head.next == None:
        return head
    new_head = func3(head.next)
    head.next.next = head
    head.next = None
    return new_head

#节点定义
class LNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#测试用例
if __name__ == '__main__':
    l1 = LNode(3)
    l1.next = LNode(2)
    l1.next.next = LNode(1)
    l1.next.next.next = LNode(99)
    l = func3(l1)
    print(l.val, l.next.val, l.next.next.val, l.next.next.next.val)

# 有图例的解法 https://blog.csdn.net/weixin_39561100/article/details/79818949



'''

class LNode:
	def __init__(self, elem, _next=None):
		self.elem = elem
		self.next_node = _next
		
 
def reverse_list(phead):
	if phead == None:
		return False
	
	new_head = None
	while phead:
		if phead.next_node == None:
			node = new_head
			new_head = phead
			new_head.next_node = node
			break
		
		tmp_head = phead.next_node
		if new_head == None:
			new_head = phead
			new_head.next_node = None
		else:
			node = new_head
			new_head = phead
			new_head.next_node = node
		
		phead = tmp_head
		
	return new_head
 
def insert_node(phead, elem):
    # 生成新的Node
	node = LNode(elem)
    # 头节点空的，则当前node是头节点
	if phead == None:
		phead = node
	else:
        # 将节点赋予 p 
		p = phead
        # 寻找尾节点
		while p.next_node:
			p = p.next_node
        # 找到尾节点后，将新节点插入
		p.next_node = node
	return phead
 
if __name__ == "__main__":
	phead = None
	for i in range(10):
		phead = insert_node(phead, i)
	p = phead
	
	while p:
		print(p.elem, end=" ")
		p = p.next_node
	
	phead = reverse_list(phead)
	p = phead
	print("")
	while p:
		print(p.elem, end=" ")
		p = p.next_node
'''

'''

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        last = None   #指向上一个节点
        while pHead:
            #先用tmp保存pHead的下一个节点的信息，
            #保证单链表不会因为失去pHead节点的next而就此断裂
            tmp = pHead.next   
            #保存完next，就可以让pHead的next指向last了
            pHead.next = last
            #让last，pHead依次向后移动一个节点，继续下一次的指针反转
            last = pHead
            pHead = tmp
        return last
    
'''  
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    