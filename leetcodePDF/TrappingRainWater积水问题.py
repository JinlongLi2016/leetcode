
def trapped_water(lst):
	if len(lst) < 2:
		return 0

	Max = 0
	MaxIdx = 0
	for idx, h in enumerate(lst):
		if h > Max:
			Max = h
			MaxIdx = idx
	if Max == 0:
		return 0

	total = 0

	peak = 0
	for i in range(MaxIdx):
		if peak > lst[i]:
			total += peak - lst[i]
		else:
			peak = lst[i]

	peak = 0
	for j in range(len(lst)-1, MaxIdx, -1):
		if peak > lst[j]:
			total += peak - lst[j]
		else:
			peak = lst[j]
	return total


def trapped_water2(hs):
	hs = [0] + hs + [0]
	acc = 0
	S = []
	for idx, height in enumerate(hs):
		if len(S) == 0:
			S.append(idx)
		elif height < hs[S[-1]]:
			S.append(idx)
		elif height == hs[S[-1]]:
			continue
		else:
			while len(S) > 1 and hs[S[-1]] < height:
				acc += (idx - S[-2] - 1) * (min(height, hs[S[-2]]) - hs[S[-1]])
				S.pop()
			if len(S) == 1:
				S.pop();
				S.append(idx)
			else:
				S.append(idx)
	return acc


print(trapped_water2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))