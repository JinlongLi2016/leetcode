# Given a collection of numbers, return all possible permutations/
# 返回一组数的所有排列


# 存在重复元素吗？

def allPermutations(lst):
	n = len(lst)

	perm = []
	process(lst, 0)

def process(lst, start):
	if start == len(lst):
		print(lst) # 一个排列
	else:
		for j in range(start, len(lst)):
			lst[start], lst[j] = lst[j], lst[start]
			process(lst, start + 1)
			lst[start], lst[j] = lst[j], lst[start]

allPermutations([1, 2, 3])