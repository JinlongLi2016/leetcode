
lst = [1, 1, 2, 2, 3]
lst = [0, 0, 0, 1, 9]
# lst = [1, 1, 2, 3]
# lst = [0, 0, 1, 1]

def all_permations(lst):
	if len(lst) == 0:
		return []

	visited = [False] * len(lst)
	a_perm = []

	forward(a_perm, lst, visited)

def forward(perm, lst, visited):
	if len(perm) == len(lst):
		print(perm)
		return 

	for i in range(len(lst)): # 这里负责把每一个未被访问且
		if visited[i]:	continue
		if i > 0 and lst[i] == lst[i-1] and (not  visited[i-1]):	continue

		perm.append(lst[i])
		visited[i] = True
		forward(perm, lst, visited)
		visited[i] = False
		perm.pop()


all_permations(lst)