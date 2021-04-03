lst = [1, 2, 3, 4 ,5, 6]

def split(A, st, end):
	i = st
	j = i + 1
	pivot = A[i]
	while j <= end:
		if A[j] < pivot:
			i += 1
			if i != j:
				A[i], A[j] = A[j], A[i]
	A[i], A[st] = A[st], A[i]
	return i 

# def topk_1(lst, k):
# 	start, end = 0, len(lst) - 1
# 	while start <= end:
# 		mid = split(lst, start, end)
# 		print(start, end)
# 		if mid==k:
# 			return lst[k]
# 		elif mid < k:
# 			start = mid + 1
# 		else:
# 			end = mid - 1



print(split(lst, 0, 5))