#!/usr/bin/env python3

import numpy as np
from random import *

# 构建Q矩阵
Q = np.zeros((6,6), np.uint8)

# 构建R矩阵，并标注联通性
R = np.ones((6,6), np.int32)
R *= -1

# 第0行
R[0,4] = 0
# 第1行
R[1,3] = 0
R[1,5] = 100
# 第2行
R[2,3] = 0
# 第3行
R[3,1] = R[3,2] = R[3,4] = 0
# 第4行
R[4,0] = R[4,3] = 0
R[4,5] = 100
# 第5行
R[5,1] = R[5,4] = 0
R[5,5] = 100

# 设定学习参数Gamma
Gamma = 0.8

# 出入口设定
Export = 5
Entrance = 2

# 开始学习
# s = randrange(0,6)    # 仅在测试中启用
s = Entrance

def learning(s):
	if s != Export:
		# 随机选择下一个房间
		All_a = []
		for i in range(0,6):
			if R[s,i] != -1:
				All_a.append(i)
		a = All_a[randrange(0,len(All_a))]
		# 记录下一个房间的所有状态
		Next_a = []
		for i in range(0,6):
			if R[a,i] != -1:
				Next_a.append(Q[a,i])
		# 更新Q矩阵
		Q[s,a] = R[s,a] + Gamma * max(Next_a)
		# 递归新状态
		if a != Export:
			learning(a)
		else:
			return
		# print(s, All_a, a)
		# print(Q)
	else:
		return
		# print('none')

# 开始经验学习
for i in range(0,1000):
	learning(s)

# # 根据学习完成的Q矩阵总结最优路径
# Best_Step = []

# def Summary(state,final):
# 	for i in range(0,6):
# 		if i == state && i != final:
# 			Best_Step.append(i)

		


print(R)