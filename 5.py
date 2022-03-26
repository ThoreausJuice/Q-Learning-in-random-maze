#!/usr/bin/env python3

# 死迷宫测试

# 构建5×5不通迷宫
import numpy as np
from random import *

# 迷宫总房间数
n = 25

# 构建R矩阵
R = np.ones((n,n), np.int32)
R *= -1

# 全通设定
for i in range(0,n):
	if i-5 >= 0:
		R[i,i-5] = 0
		R[i-5,i] = 0
	if i+5 <= 24:
		R[i,i+5] = 0
		R[i+5,i] = 0
	if (i-1)%5 != 4:
		R[i,i-1] = 0
		R[i-1,i] = 0
	if (i+1)%5 != 0:
		R[i,i+1] = 0
		R[i+1,i] = 0

# 关闭终点设定
R[23,24] = -1
R[19,24] = -1
R[24,24] = 100

# 构建Q矩阵
Q = np.zeros((n,n), np.uint8)

# 出入口设定
Export = 24
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

for i in range(0,100):
	Mouse(Entrance, 0)

label = 0
for i in range(0,n):
	for j in range(0,n):
		if Q[i,j] != 0:
			label += 1

if label == 0:
	print("该迷宫为死迷宫")
else:
	print("该迷宫有出路")