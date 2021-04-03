

def isBalancedTree(T):
	return balancedTreeHeight(T) >= 0


def balancedTreeHeight(T):
	'''return the hight of T
	
	如果不是平衡树，返回-1，否则返回树高
	'''
	if T is None:
		return 0
	left = balancedTreeHeight(T.left)
	right = balancedTreeHeight(T.right)

	if left < 0 or right < 0 or abs(left-right) > 1:
		return -1
	return max(left, right)


