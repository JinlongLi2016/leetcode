

A = "aabcc"
B = "dbbca"
# C = "aadbbcbcac"
C = "aadbbbaccc"

A, B, C = 'a', 'b', 'ba'

# DFS, 会超时
def func(S, p, i, j):
	if i == len(A) and j == len(B):
		return True
	if i == len(A):
		return func(S, p+1, i, j+1) if B[j] == C[p] else False
	elif j == len(B):
		return func(S, p+1, i+1, j) if A[i] == C[p] else False
	else:
		result = False
		if result==False and C[p]==A[i]:
			result = func(S, p+1, i+1, j)
		if (result==False) and C[p] == B[j]:
			result = func(S, p+1, i, j+1)
		return result

print(func([], 0, 0, 0))