
def allC(lst, k): #
	print(lst, k)
	if len(lst) <  k or k==0:
		return [[ ]]
	elif len(lst) == k:
		return [lst]
	else:
		tmp_C = [l + [lst[0]] for l in allC(lst[1:], k-1)]
		return tmp_C + allC(lst[1:], k)

print(allC([1, 2, 3], 2) ) 