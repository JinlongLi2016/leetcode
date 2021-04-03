#coding:utf-8
steps = []
# steps[i] 表示在i处，能够跳几步。

def minimum_steps(steps):
	f = [100] * len(steps); f[0] = 0
	last_point = 0
	
	i = 0
	while i < len(steps) and i <= last_point:
		# 开始处理i处的情况，对于i能到的所有地方p，计算f[p]的最小值  f[p] = min(f[p], f[i] + 1)
		last_point = max(last_point, i + steps[i])

		for j in range(steps[i]):
			if i+j+1 >= len(steps):	break
			f[i+ j+1] = min(f[i+ j+1], f[i] + 1)
		i += 1

	if i >= len(steps) - 1:
		return f[-1]
	else:
		return -1

def minimum_steps2(steps):
	'''另一种方式是 尝试从每一层跳到最远'''
	left, right = 0, 0 # [left, right]
	step = 0

	# 下一层的起点是right，终点是？
	while right < len(steps)-1:
		new_right = right
		for i in range(left, right+1):
			new_right = max(new_right, i + steps[i])
		left, right = right+1, new_right
		step += 1
	print(right)
	return step 

def minimum_steps3(steps):
	i = j = 0
	step_num = 1
	j = i + steps[i]
	while j < len(steps) - 1:
		maxflag = i 
		nxt_idx = i
		for k in range(i+1, j+1):
			if k + steps[k] > maxflag:
				nxt_idx = k 
				maxflag = k + steps[k]
		i = nxt_idx
		step_num += 1
		j = i + steps[i]
	return step_num



print(minimum_steps3([2,3,1,1,4, 1, 1]))