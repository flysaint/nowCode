# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 22:10:39 2019

@author: fly_s

BaseImprove_Class07_Code04_HorseJump

题目四
象棋中马的跳法
【题目】
请同学们自行搜索或者想象一个象棋的棋盘，然后把整个棋盘放入第一象限，棋盘的最左下
角是(0,0)位置。那么整个棋盘就是横坐标上9条线、纵坐标上10条线的一个区域。给你三个
参数，x，y，k，返回如果“马”从(0,0)位置出发，必须走k步，最后落在(x,y)上的方法数
有多少种？

# basecase 边界条件有哪些
换个方式思考，从x,y位置，经过k步，达到(0,0)位置有多少种可能。
因此 x,y,k 代表就是上面的意思。

"""

def process(x,y,k):
    
    # 越界的情况
    if x < 0 and x > 8 and y < 0 and y > 9:
        return 0
    
    # 已经没有步数的情况
    if k == 0:
        if x == 0 and y == 1:
            return 1
        else:
            return 0
        
        
    # 一般过程，是从马的其他8个位置跳到x,y的可能
    return process(x - 1, y + 2, step - 1)
				+ process(x + 1, y + 2, step - 1)
				+ process(x + 2, y + 1, step - 1)
				+ process(x + 2, y - 1, step - 1)
				+ process(x + 1, y - 2, step - 1)
				+ process(x - 1, y - 2, step - 1)
				+ process(x - 2, y - 1, step - 1)
				+ process(x - 2, y + 1, step - 1)
    




























