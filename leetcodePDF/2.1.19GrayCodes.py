
def all_gray_codes(n):
	lst = [None] * n
	procede(0, lst)

def procede(i, lst):
	if i == len(lst):
		print(lst)
	else:
		for p in [0, 1]:
			lst[i] = p
			procede(i+1, lst)
		lst[i] = None

all_gray_codes(3)