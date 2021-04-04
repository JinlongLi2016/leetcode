# Given a set of distinct integers, S,return all possible subsets. 


def subsets1(lst):
	if len(lst)==1:
		return [lst]
	e = lst.pop()
	presubsets = subsets(lst)
	newsubsets = [l + [e] for l in presubsets] + [[e]]
	return presubsets + newsubsets
	#  这个函数返回的没有空集，因此把这个函数作为过程来调用的主函数应该加上一个空集


def subsets(lst):
	if len(lst) == 0:
		return [[]]
	e = lst.pop()
	presubsets = subsets(lst)
	newsubsets = [l + [e] for l in presubsets] 

	return presubsets + newsubsets

	# two list addition will return a new list

# 可以使用深度优先搜索？ using a vector.
# This can apply to existing duplicate elements case.


# 如果存在

print(subsets([1, 2, 2, 3]))

## 另外一种方式，考虑位向量
 一共有 2^n 种排列方式（包括空集），如果n位二进制数 某一位位1 意味着其对应的这个元素在集合中，否则就不在集合中。
 如果用整数来表征这种位向量，受到整数位数的影响。但是可以很方便地求并、交