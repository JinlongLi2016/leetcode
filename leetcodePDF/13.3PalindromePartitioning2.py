# 如何动态规划这道题
# 字符串回文划分,要求以最小划分次数划分成回文子串

string = 'helloworld'

class array(object):
	"""docstring for array"""
	def __init__(self, m, n):
		super(array, self).__init__()
		self._data = [None] * m * n
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

def palindrome_mincuts(s):
	'''return minimum cuts of the string
	
	s: the string
	return:
		int 
	'''
	n = len(s)
	f = list(range(-1, n))
	f.reverse()
	P = array(len(s), len(s))
	for i in range(n):
		for j in range(n):
			P[i, j] = False
	# P[i, j], [i, j]间字符 是否位回文串
	# f[i] [i, +inf)间字符的最小划分次数

	for i in range(n-1, -1, -1):
		for j in range(i, n):
			if s[i]==s[j] and (j-i<2 or P[i+1, j-1]==True):
				P[i, j] = True
				f[i] = min(f[i], f[j+1] + 1)
	return f[0]

print(palindrome_mincuts('aaaabbbbb'))


