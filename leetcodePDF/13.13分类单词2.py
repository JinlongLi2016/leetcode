# 打断字符串

d = ['cat', 'cats', 'dog', 'and', 'sand']


# Solution: 深度优先遍历 （世间复杂度可能较高）

def break_word_dfs(String, Dict):
	result = []

	def forward(S, path):
		if len(S)==0:
			result.append(' '.join(path)) 
			return
		for i in range(len(S)):
			if S[:i+1] in Dict:
				path.append(S[:i+1])
				split(S[i+1:], path)
				path.pop()

	forward(String, [])
	return result

# Solution: DP  f[i]: 表示字符S[i]前面是否可以划分。
# 比如f[0]表示字符S[0]前面是否可以划分 f[len(S)] 表示S[len(S)]前面是否可以划分
def break_word_dp(String, Dict):
	f = [False] * (len(String) + 1)
	f[0] = True

	# for i in range(len(String)): # 

	# 	# 判断j到下标为i的字符是否可划分 
	# 	for j in range(i, -1, -1): # [j:i+1]
	# 		if String[j:i+1] in Dict and f[j]==True:
	# 			f[i+1] = True
	# 			break 

	#  I prefer the following codes.
	i = 1
	while i <= len(String): # fill f[i]
		j = i - 1
		while j >= 0:
			if String[j:i] in Dict and f[j]==True:
				f[i] = True
				break 
			j -= 1
		i += 1

	result = []

	def forward(S, path):
		if len(S) == 0:
			result.append(path.copy())
			return
		for i in range(len(S)-1, -1, -1): # 从最后一个下标开始
			if S[i:] in Dict and f[len(S)]==True: # S后面是可分的
				path.append(S[i:])
				forward(S[:i], path)
				path.pop()
				
	forward(String, [])

	return result


print(break_word_dp('catsanddog', d))