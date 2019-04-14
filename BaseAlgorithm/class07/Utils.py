# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:13:09 2019

@author: DELL
"""


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

def cmp3(o1,o2):
    return o1.end - o2.end
















