'''
https://leetcode-cn.com/problems/distinct-subsequences/
S的子序列为T的子序列数量


假设F[i, j] 为 T[0:j] 在 S[0:i]里面出现的次数
如果不使用S[i]:
	f[i, j] = f[i-1, j]
如果使用S[i]:(前提是Si == Tj)
	f[i, j] = f[i-1, j-1] + f[i-1, j] 



Furthur Analysis: 
	如果S最后一个字母不使用的话，有多少个不同子序列？ 如果最后一个字母使用的话，有多少个不同的子序列？
'''

class array(object):
	"""docstring for array"""
	def __init__(self, m, n, value=None):
		super(array, self).__init__()
		self._data = [value] * m * n
		self._rows = m
		self._cols = n

	def __getitem__(self, key):
		row, col = self._validate_key(key)
		return self._data[row*self._cols+col]

	def __setitem__(self, key, value):
		row, col = self._validate_key(key)
		self._data[row*self._cols+col] = value

	def _validate_key(self, key):
		row, col = key
		if (0 <=row < self._rows and
			0 <= col < self._cols):
			return key 
		raise KeyError("Subscript out of range {}".format(key))

	def __repr__(self):
		l = []
		for i in range(self._rows):
			l.append([None] * self._cols)
		for i in range(self._rows):
			for j in range(self._cols):
				l[i][j] = self.__getitem__([i, j])
		return str(l)

def distinct_subsequence(S, T):
	m, n = len(S), len(T) # m >= n
	f = array(m, n, 0)
	f[0, 0] = 1 if S[0] == T[0] else 0
	for i in range(1, n):
		f[i, i] = 1 if f[i-1, i-1]>0 and S[i] == T[i] else 0

	for i in range(1, m):
		f[i, 0] = 0

	for j in range(1, n):
		for i in range(j+1, m):
			if S[i] == T[j]:
				f[i, j] = f[i-1, j-1] + f[i-1, j]
			else:
				f[i, j] = f[i-1, j]
	print(f[m-1, n-1])

print(distinct_subsequence("rabbbit", "rabit"))