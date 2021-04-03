def solution(nums, target):
	# @todo: check nums's size is at least 3
	# all numbers are posivie?
	nums.sort()
	# removeduplicates(nums)
	#  夹逼怎么做？ 夹逼的时间复杂度到位
	i, j = 0, len(nums) - 1
	twoSum = nums[i] + nums[j]

	while  i < j and twoSum + nums[i+1] != target:
		if(twoSum >= target):
			j -= 1
			twoSum = nums[i] + nums[j]
		else:
			properNum = target - twoSum
			# idx = binarySearch(nums, i+1, j, properNum)
			idx = nums.index(properNum)
			print(idx)
			if idx > 0:
				print(nums[i], nums[idx], nums[j])
			i += 1

lst = list(range(10))
solution(lst, 15)