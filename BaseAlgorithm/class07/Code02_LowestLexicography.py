# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:28:24 2019

@author: DELL
给定一个字符串类型的数组strs，找到一种拼接方式，使得把所有字符串拼起来之后形成的
字符串具有最小的字典序。
https://blog.csdn.net/as1171799253/article/details/83685615?tdsourcetag=s_pcqq_aiomsg
"""

def lowestString(strs):
    if strs is None or len(strs) == 0:
        return "";
    
    strs = sorted(strs,lambda x)
 

testItems = [(2, [3, 4, 5]), (3, [1, 0, 0, 0, 1]), (4, [-1]), (10, [1, 2, 3])]

def myComparator(a,b):
    print ("Values(a,b): ",(a,b))
    sum_a=sum(a[1])
    sum_b=sum(b[1])
    print (sum_a,sum_b)
    print ("Comparision Returns:",cmp(sum_a,sum_b))
    return cmp(sum_a,sum_b)

testItems.sort(myComparator)
print(testItems)










