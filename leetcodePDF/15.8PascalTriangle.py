# pascal 三角形

numRows = 5
result = []
result.append([1])

prev_lst = [0] + [1] + [0]
for _ in range(numRows):
	nxt_lst = [0]

	for i in range(len(prev_lst) - 1):
		nxt_lst.append(prev_lst[i] + prev_lst[i+1])
	
	result.append(nxt_lst[1:].copy())
	nxt_lst.append(0)
	prev_lst = nxt_lst

print(result)