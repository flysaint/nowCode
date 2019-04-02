# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 14:00:59 2019

@author: DELL
"""

import random

def isEqual(arr1,arr2):
    if((arr1 is None and arr2 is not None) or (arr1 is not None and arr2 is None )):
        return False
    if(arr1 is None and arr2 is None):
        return True
    arr1Len = len(arr1)
    arr2Len = len(arr2)
    if( arr1Len != arr2Len):
        return False
    for i in range(arr1Len):
        if(arr1[i] != arr2[i]):
            return False
    return True

def ArrayCompare(arrFunction,testTime = 500 ,maxSize = 50,maxValue = 100):
    for i in range(0,testTime):
        testArr1 = random.sample(range(0,testTime),maxSize)
        testArr2 = testArr1.copy()
        testArr1 = arrFunction(testArr1)
        (testArr2).sort()
        if not isEqual(testArr1,testArr2):
            print('the function is not rigit!')
    print('Congratulations, the function is correct!')
    
    
    
    
    
    
    
    
    