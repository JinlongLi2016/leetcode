
# 非递归中序遍历
# 时空复杂度均为O(n)
def inorder_traversal(T):
	st = []
	last = float('-inf')
	while T or len(st) > 0:
		while T:
			st.append(T)
			T = T.left
		T = st.pop()
		if T.val < last.val:
			return False
		last = T
		T = T.right
	return True


