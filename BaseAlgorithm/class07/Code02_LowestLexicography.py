# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:28:24 2019

@author: DELL
给定一个字符串类型的数组strs，找到一种拼接方式，使得把所有字符串拼起来之后形成的
字符串具有最小的字典序。
https://blog.csdn.net/as1171799253/article/details/83685615?tdsourcetag=s_pcqq_aiomsg
"""
import functools
import os
os.chdir(r"D:/Code/github/nowCode/nowCode/BaseAlgorithm/class07/")

import Utils


def getEqualLen(a,b):
    if len(a) > len(b):
        b = b + '0'*(len(a) - len(b))
    elif len(a) < len(b):
        a = a + '0'*(len(b) - len(a))
    return a,b

def cmp(a,b):
    for i in range(len(a)):
        if ord(a[i]) - ord(b[i]) == 0:
            continue
        else:
            return ord(a[i]) - ord(b[i])
    return 0

def cmp1(a, b):
    a,b = getEqualLen(a,b)
    return cmp(a,b)

def cmp2(a, b):
    return cmp1(a+b,b+a)


def lowestString(strs):
    if strs is None or len(strs) == 0:
        return ""
    strs.sort(key=functools.cmp_to_key(Utils.cmp2))
    
    return ''.join(strs)
    
if __name__ == '__main__':
 
    test_list = ["jibw", "ji", "jp", "bw", "jibw" ]
    # test_list.sort(key=functools.cmp_to_key(lambda a,b: a.x-b.x if a.x != b.x else a.y-b.y))
    print(lowestString(test_list))
    test_list2 = ['ba','b']
    # sorted(test_list, key=functools.cmp_to_key(cmp))  #    亲测此方法不能成功排序
    print(lowestString(test_list2))





