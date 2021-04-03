
def MaxRectangleInHist(hist):
	st = [0]
	hist.insert(0, 0)
	hist.append(0)
	maxArea = 0

	# 维护一个递增栈
	# 当遍历到的元素小于栈顶元素，那么栈顶元素的左右两侧小于它的边界就找到了
	# 在左侧添加0，为了避免对栈判空；右侧添加0，是为了清空栈，设想一下如果hist是递增序列。
	# for i in range(len(hist)):
	# 	if hist[st[-1]] < hist[i]:
	# 		st.append(i)
	# 	elif hist[st[-1]] > hist[i]:
	# 		while hist[st[-1]] > hist[i]:
	# 			area = hist[st[-1]] * (i - st[-2] - 1)
	# 			maxArea = max(maxArea, area)
	# 			st.pop()
	# 		st.append(i)
	for i in range(len(hist)):
		if hist[st[-1]] > hist[i]:
			while hist[st[-1]] > hist[i]:
				area = hist[st[-1]] * (i - st[-2] - 1)
				maxArea = max(maxArea, area)
				st.pop()
		st.append(i)

	return maxArea
print(MaxRectangleInHist([2,1,5,6,2,3]))


def maxRectangle(hist):
	if len(hist) < 1:
		return 0
	elif len(hist) == 1:
		return hist[0]
	hist = [0] + hist + [0]
	leftH = [0] * len(hist)
	rightH = [0] * len(hist)

	for i in range(1, len(hist)-1):
		if hist[i] > hist[i-1]:
			leftH[i] = i - 1
		elif hist[i] == hist[i-1]:
			leftH[i] = leftH[i-1]
		else:
			j = i -1
			while hist[j] >= hist[i]:
				j = leftH[j]
				# print(j)
				if j == 0:
					break 

			leftH[i] = j
	
	rightH[len(hist)-1] = len(hist) -1
	for i in range(len(hist)-2, 0, -1):
		if hist[i] > hist[i+1]:
			rightH[i] = i + 1
		elif hist[i] == hist[i+1]:
			rightH[i] = rightH[i+1]
		else:
			j = i + 1
			while hist[j] >= hist[i]:
				j = rightH[j]
				if j == len(hist) - 1:
					break 
			rightH[i] = j


	print(leftH)
	print(rightH)
	MaxArea = 0
	for i in range(1, len(hist)-1):
		area = hist[i] * (rightH[i] - leftH[i]-1)
		MaxArea = max(area, MaxArea)
	print(MaxArea)

# maxRectangle([2, 1, 5, 6, 2, 3])
# maxRectangle([0,1,0,2,1,0,1,3,2,1,2,1])
