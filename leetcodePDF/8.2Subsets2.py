# 存在重复元素，还能够使用8.1的解法？
# 8.1解法是基于 n-1个元素的所有子集构造n个元素的所有子集
# 在8.2中，由于有重复元素，故不能够原封不动地借用。 可以对每个distinct的数字
# 计算他们的所有子集，再扩展到第n个distinct数字上面。扩展的时候需要考虑nth distinct
# 数字的个数。

# 另一种解法是用DFS来做

from collections import defaultdict
lst = [1, 2, 2, 3]
def allsubsets(lst):
	cnt = defaultdict(int)	
	for l in lst:
		cnt[l] += 1

	elements = list(cnt.keys())
	S = [0] * len(cnt.keys())

	helper(S, elements, 0, len(S), cnt)


def helper(S, elements, m, last, volumn):
	if m == last: # one set
		#print(S)
		S2set(S, elements)
		return 
	for num in range(volumn[elements[m]] + 1):
		S[m] = num 
		helper(S, elements, m+1, last, volumn)
		# S[m] = 0

def S2set(s, elements):
	#print(elements, s)
	lst = []
	# lst = [[e] * si for e, si in (zip(elements, s))]
	for e, si in zip(elements, s):
		lst += [e] * si
	print(lst)


allsubsets(lst)