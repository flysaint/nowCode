# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:09:23 2019

@author: fly_s
案例1）一个数组中有一种数出现了奇数次，其他数都出现了偶数次，怎么找到这一个数
案例2）一个数组中有两种数出现了奇数次，其他数都出现了偶数次，怎么找到这两个数
"""
#案例1
def printOddTimesNum1(arr):
    eO = 0
    for cur in arr:
        eO ^= cur
    return eO
#案例2
def printOddTimesNum2(arr):
    eO = 0
    eOhasOne = 0
    for curNum in arr:
        eO ^= curNum
        #eO = a^b
		#eO != 0
		#eO必然有一个位置上是1
		#么取一个二进制数，最右边的1？ 取反+1，再与原二进制求与（经常用，手动试试就知道）
    rightOne = eO & (~eO + 1)
    for cur in arr:
        # 取!= 或 == 都可以，因为每次只找一边
        if (cur & rightOne) != 0:
            eOhasOne ^= cur
    print('a = {},b = {}'.format(eO,eO^eOhasOne))



