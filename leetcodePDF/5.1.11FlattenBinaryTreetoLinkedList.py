
def flattenT(T, pre):
	if(T):
		Tleft, Tright = T.left, T.right
		pre[0].right = T 
		T.left = pre[0]
		prev[0] = T
		FlattenT(Tleft, prev)
		FlattenT(Tright, prev)

def FlattenBT(T):
	head = p = BTNode()
	prev = [p]
	FlattenT(T, prev)
	
	prev[0].right = None

	return head.right

# 2019.9.29
# 时空复杂度是多少
def flattenBT(T):
	if T is None:
		return 
	flattenBT(T.left)
	flattenBT(T.right)

	# Merge two subtree
	p = T.left
	if p is None:	return 

	while p.right:
		p = p.right 
	p.right = T.right
	T.right = T.left

	T.left = None 