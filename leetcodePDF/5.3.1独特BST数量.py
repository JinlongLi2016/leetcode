
def unique_bst_num(n):
	assert isinstance(n, int), "input param should be integer, but got {}".format(type(n))

	if  n < 3:
		return n 
	lst = [0] * (n+1)
	lst[0] = 1
	lst[1] = 1
	lst[2] = 2


	for i in range(3, n+1):
		for j in range(i):
			lst[i] += lst[j] * lst[i-j-1]

	return lst[n]
	# O(n^2)

print(unique_bst_num(5))