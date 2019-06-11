

'''
w = [2, 3, 5, 7]
v = [1, 5, 2, 4]
bag = 10
max_value = 9

'''


def process(w,v,index,rest):
	
	# 处理边界情况
	# 已经超过最后的位置
	if index == len(w) :
		return 0 
	
	# 背包已经没有空间了
	if rest <= 0:
		return 0
		
	# 不用当前位，的情况	
	p1 = process(w,v,index + 1,rest)
	
	# 使用当前位，的情况.
	
	# 问题1：此时没有考虑，使用当前位置后，rest 小于 0的情况 
	#p2 = v[index] + process(w,v,index,rest - w[index])
	
	# 剩余的空间，要大于本次消耗的空间
	# 初始化p2 为负值，这样让不选择index位置时，保证只考虑p1的情况
	p2 = -1
	if rest > w[index]:
		p2 = v[index] + process(w,v,index + 1,rest - w[index])
	
	return max(p1,p2)

import numpy as np

weight = [2, 3, 5, 7]
value = [1, 5, 2, 4]
weight_most=10

rest = 10
w = weight
v =  value

w_len = len(w)  
dps = np.zeros((w_len+1,rest+1),dtype=np.int32)
for index in range(w_len-1,-1,-1):
    for rest_index in range(0,rest):
        dps[index,rest_index] = dps[index + 1,rest_index]
        if rest_index + w[index] <= rest:
            dps[index,rest_index] = max(v[index] + dps[index+1,rest_index - w[index]],\
               dps[index,rest_index])




def process2(w,v,rest):
	
    w_len = len(w)  
    dps = np.zeros((w_len+1,rest+1),dtype=np.int32)
    for index in range(w_len-1,0,-1):
        for rest_index in range(rest,0,-1):
            dps[index,rest_index] = dps[index + 1,rest_index]
            if rest_index + w[index] <= rest:
                dps[index,rest_index] = max(v[index] + dps[index+1,rest_index + w[index]],\
                   dps[index,rest_index])
    return dps[0][0]
        
process2(weight,value,weight_most)	
	

 
weight=[2,2,6,5,4]
value=[3,6,5,4,6]
weight_most=10

weight = [2, 3, 5, 7]
value = [1, 5, 2, 4]
weight_most=10


def bag_0_1(weight,value,weight_most):#return max value
    num = len(weight)
    weight.insert(0,0)#前0件要用
    value.insert(0,0)#前0件要用
    bag=np.zeros((num+1,weight_most+1),dtype=np.int32)#下标从零开始
    for i in range(1,num+1):
        for j in range(1,weight_most+1):
            if weight[i]<=j:
                bag[i][j]=max(bag[i-1][j-weight[i]]+value[i],bag[i-1][j])
            else:
                bag[i][j]=bag[i-1][j]
    # print(bag)
    return bag[-1,-1]
 
result=bag_0_1(weight,value,weight_most)
print(result)



def process3(m, A, V):
    n = len(A)
    if m <= 0 or n <= 0:
        return 0
    dp = [0 for _ in range(m + 1)]
    for i in range(n):
        for j in range(m,A[i]-1,-1):
            dp[j] = max(dp[j-A[i]]+V[i], dp[j])














			