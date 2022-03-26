#!/usr/bin/env python3

# 加强版小老鼠

# 构建5×5随机迷宫
import numpy as np
from random import *

# 初始化R矩阵
R = np.ones((25,25), np.int32)
R *= -1

# 随机构建连通性
for i in range(0,25):
	# 记录每个房间的邻居
	Recording = []
	if i-5 >= 0:
		Recording.append(i-5)
	if i+5 <= 24:
		Recording.append(i+5)
	if (i-1)%5 != 4:
		Recording.append(i-1)
	if (i+1)%5 != 0:
		Recording.append(i+1)
	# 打乱邻居列表的顺序
	shuffle(Recording)
	# 随机出至少一个邻居使其与之相通
	j = randrange(1,len(Recording)+1)
	for k in range(0,j):
		R[i,Recording[k]] = 0
		R[Recording[k],i] = 0

# 出入口设定
Export = randrange(0,25)
Entrance = randrange(0,25)

# 出口值奖励系数修正
for i in range(0,25):
	if R[i,Export] == 0:
		R[i,Export] = 100

# 构建Q矩阵
Q = np.zeros((25,25), np.uint8)

# 设定学习参数Gamma
Gamma = 0.8

# 开始学习
s = Entrance
time = 0

def learning(s, time):
	if s != Export:
		# 随机选择下一个房间
		All_a = []
		for i in range(0,25):
			if R[s,i] != -1:
				All_a.append(i)
		a = All_a[randrange(0,len(All_a))]
		# 记录下一个房间的所有状态
		Next_a = []
		for i in range(0,25):
			if R[a,i] != -1:
				Next_a.append(Q[a,i])
		# 更新Q矩阵
		Q[s,a] = R[s,a] + Gamma * max(Next_a)
		# 递归新状态
		if a != Export and time < 26:
			time += 1
			learning(a, time)
		else:
			return
	else:
		return

# 开始经验学习
for i in range(0,100):
	learning(s, time)

# 给出其中一种最优解
List_of_Optimal_solutions = []

def Optimal_Solution(s):
	if s != Export and len(List_of_Optimal_solutions) < 26:
		List_of_Optimal_solutions.append(s)
		Value_Recording = []
		Position_Recording = []
		for i in range(0,25):
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
Optimal_Solution(s)

print(List_of_Optimal_solutions)

# print(Q)