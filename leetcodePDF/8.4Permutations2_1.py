from collections import defaultdict 

lst = [1, 2, 1, 3, 4, 4]
lst = [1, 1, 2]
cnter = defaultdict(int)
for l in lst:
	cnter[l] += 1
path = [None] * len(lst)

def perm(lst):
	p(0)

def p(i):
	if i >= len(lst):
		print(path)
	else:
		for k in cnter.keys():
			if cnter[k] > 0:
				cnter[k] -= 1; path[i] = k
				p(i+1)
				cnter[k] += 1; 

# I think this type of coding is better. Path用于存储每一种可能，同时在从左到右构造每一位数字时，都保证不会有第二个相同的数字在同一位出现，
# 因此internally，不会构造出两个一样的序列 

perm(lst)