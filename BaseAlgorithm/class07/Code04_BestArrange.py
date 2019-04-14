# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:14:03 2019

@author: DELL

一些项目要占用一个会议室宣讲，会议室不能同时容纳两个项目的宣讲。
给你每一个项目开始的时间和结束的时间(给你一个数 组，里面是一个个具体
的项目)，你来安排宣讲的日程，要求会议室进行的宣讲的场次最多。
返回这个最多的宣讲场次。

"""
import functools

class Program:
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
    def __str__(self):
        return ('(%s,%s)' % (self.start,self.end))
    
    __repr__ = __str__
        
def cmp3(o1,o2):
    return o1.end - o2.end

def bestArrange(programs,start):
    programs.sort(key=functools.cmp_to_key(cmp3))
    
programs = [Program(1,2),Program(2,3),Program(1,1)]

print(programs)
programs.sort(key=functools.cmp_to_key(cmp3))

print(programs)















