# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 11:29:03 2019

@author: fly_s
"""
import random

def find(arr,v):
    
    if arr is None or len(arr) == 0:
        return False
    if len(arr) == 1 and arr[0] != v:
        return False
    
    l = 0
    r = len(arr) - 1
    mid = l + int((r - l)/2)
    if (arr[mid] == v):
        return True
    elif arr[mid] > v:
        left = arr[:mid]
        return find(left,v)
    else:
        right = arr[mid+1:]
        return find(right,v)
    
def find(arr,v):
    if arr is None or len(arr) == 0:
        return False
    if len(arr) == 1 and arr[0] != v:
        return False
    
    l = 0
    r = len(arr) - 1
    mid = l + int((r - l)/2)
    


def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
        
     
testArr = sorted(random.sample(range(100),10))
   
 
find(testArr,testArr[0] - 1)














