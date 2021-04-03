'''
两个字符串，对一个字符串的操作可以等价地转换为对另外一个字符串的操作。
因此可以只操作一个字符串，把另外一个字符串作为target。

动态规划这道题：f[i, j] indicating A 前i个字符 和B前j个字符的最小编辑距离

那么如果 A[i] == B[j]:
	f[i,j] = f[i-1, j-1]
如果 A[i] != B[j]:
	f[i, j] = f[i, j-1] + 1, A[i] != B[j], 在Ai后面添加字母Bj
	f[i, j] = f[i-1, j-1] + 1, Ai 替换为Bj
	f[i, j] = f[i-1, j] + 1, 删除Ai

'''

import array
s1, s2
def edit_distance(s1, s2):
	m, n = len(s1), len(s2)

	f = array.array(m+1, n+1)
	for i in range(m+1):
		f[i, 0] = 0
	for j in range(n+1):
		f[0, j] = 0

	for i in range(1, m+1):
		for j in range(1, n+1):
			if s1[i-1] == s2[j-1]:
				f[i, j] = f[i-1, j-1]
			else:
				f[i, j] = min(f[i, j-1], f[i-1, j], f[i-1, j-1]) + 1
	print(f[m, n])

# 可以改为用滚动数组来实现。（所谓的滚动数组其实就是dp里面不存整个table，而只存两行