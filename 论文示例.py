#!/usr/bin/env python3

import numpy as np
from random import *

# 迷宫总房间数
n = 9

# 构建Q矩阵
Q = np.zeros((n,n), np.uint8)

# 构建R矩阵
R = np.ones((n,n), np.int32)
R *= -1

R[0,1] = 0

R[1,0] = 0
R[1,4] = 0

R[2,5] = 0

R[3,4] = 0

R[4,1] = 0
R[4,3] = 0
R[4,5] = 0
R[4,7] = 0

R[5,4] = 0
R[5,2] = 0
R[5,8] = 0

R[6,7] = 0

R[7,4] = 0
R[7,6] = 0
R[7,8] = 0

R[8,5] = 0
R[8,7] = 0

R[7,6] = 100

# 出入口设定
Export = 6
Entrance = 0

# 设定学习参数Gamma
Gamma = 0.8

def Mouse(s, x):
	if s != Export and x <= n:
		# 记录下一个房间的所有情况
		All_a = []
		for i in range(0,n):
			if R[s,i] != -1:
				All_a.append(i)
		# 随机选择下一个房间
		a = All_a[randrange(0,len(All_a))]
		# 记录下一个状态的所有Q矩阵值
		Next_a = []
		for i in range(0,n):
			if R[a,i] != -1:
				Next_a.append(Q[a,i])
		# 更新Q矩阵
		Q[s,a] = R[s,a] + Gamma * max(Next_a)
		# 递归新状态
		if a != Export and x <= n:
			Mouse(a, x+1)
		else:
			return
	else:
		return

for i in range(0,1000):
	Mouse(Entrance, 0)

print(Q)

# 给出其中一种最优解
List_of_Optimal_solutions = []

def Optimal_Solution(s):
	if s != Export and len(List_of_Optimal_solutions) < 26:
		List_of_Optimal_solutions.append(s)
		Value_Recording = []
		Position_Recording = []
		for i in range(0,n):
			if Q[s,i] != 0:
				Value_Recording.append(Q[s,i])
				Position_Recording.append(i)
		for i in range(0,len(Value_Recording)):
			if Value_Recording[i] == max(Value_Recording):
				Next_Position = Position_Recording[i]
		Optimal_Solution(Next_Position)
	elif s == Export:
		List_of_Optimal_solutions.append(s)
		return
	else:
		return

Optimal_Solution(Entrance)

print(List_of_Optimal_solutions)
