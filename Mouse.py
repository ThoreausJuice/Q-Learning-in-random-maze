#!/usr/bin/env python3

from random import *

# Q-Learning 核心算法
# 需要给小老鼠传入5个参数：当前位置，出口位置，房间总数，当前步数，Q矩阵，R矩阵
# 函数将会返回最终收敛的Q矩阵

def Mouse(now, x):
	if now != Export or x <= n:
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
		if a != Export or x <= n:
			Mouse(a, x+1)
		else:
			return
	else:
		return