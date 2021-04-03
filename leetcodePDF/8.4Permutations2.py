
lst = [1, 1, 2, 2, 3]
lst = [0, 0, 0, 1, 9]
# lst = [1, 1, 2, 3]
# lst = [0, 0, 1, 1]

def all_permations(lst):
	if len(lst) == 0:
		return []
	forward(lst, 0)

def forward(lst, m):
	if m == len(lst):
		print(lst)
		return 

	last_element = None
	for j in range(m, len(lst)):
		if last_element == lst[j]:
			continue
		last_element = lst[j]

		lst[j], lst[m] = lst[m], lst[j]
		forward(lst, m+1)
		lst[j], lst[m] = lst[m], lst[j]

all_permations(lst)