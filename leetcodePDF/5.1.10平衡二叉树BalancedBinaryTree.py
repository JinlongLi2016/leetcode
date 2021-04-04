'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two
subtrees of every node never differ by more than 1
'''

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


