# 先解决直方图中矩形最大面积问题

hist = [6,2,5,4,5,1,6]

def max_size(hist):
	st = []
	MaxSize = 0

	for i, h in enumerate(hist):
		if len(st)==0 or hist[st[-1]] < h:
			st.append(i)
		elif hist[st[-1]] == h:
			continue
		else:
			while len(st) > 0 and hist[st[-1]] > h:
				tmp_h = hist[st.pop()] # 确定左边界的方式
				left_border = st[-1] if len(st)>0 else -1
				MaxSize = max(MaxSize, tmp_h * (i-left_border-1))
			st.append(i)

	while len(st) > 0:
		tmp_h = hist[st.pop()]
		left_border = st[-1] if len(st)>0 else -1
		MaxSize = max(MaxSize, tmp_h * (len(hist) - left_border-1))
	return MaxSize

print(max_size(hist))

