# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:45:11 2019
@author: fly_s
查找和排序
题目：输入任意（用户，成绩）序列，可以获得成绩从高到低或从低到高的排列,相同成绩
都按先录入排列在前的规则处理。
示例：
jack      70
peter     96
Tom       70
smith     67

从高到低  成绩 
peter     96 
jack      70 
Tom       70 
smith     67

从低到高
smith     67
jack      70 
Tom       70 
peter     96
"""

# 方案1
while True:
    try:
        dic=[]
        a,b=int(input()),input()
        isDesc=True if b=="0" else False
        for i in range(a):
            name, score = input().split()
            dic.append((name,int(score)))
        if isDesc:
            for i in sorted(dic, key=lambda item: (item[1],-dic.index(item)), reverse=isDesc):
                print(i[0] + " " + str(i[1]))
        else:
            for i in sorted(dic, key=lambda item: (item[1],dic.index(item))):
                print(i[0] + " " + str(i[1]))
    except:
        break


# 方案2
while True:
    try:
        n,flag,grade = int(input()),int(input()),[]
        for i in range(n):
            In = input().split()
            grade.append([In[0],int(In[1])])
        grade = sorted(grade,key = lambda x:x[1],reverse = not flag)
        for each in grade:
            print(each[0],each[1])
    except:
        break

# 方案3
while True:
    try:
        num = int(input())
        whetherRev = (int(input())!=1)
        students = []
        for i in range(num):
            students.append(input().split())
        students.sort(key=lambda x:int(x[1]),reverse=whetherRev)
        for i in students:
            print(" ".join(i))
    except Exception:
        break
    



'''