
arr = [5, 7, 7, 8, 8, 10]
target = 0

def first_criteria(idx):
	if arr[idx] == target and (idx==0 or arr[idx-1] < target):
		return True
	return False
def last_criteria(idx):
	if arr[idx] == target and  (idx ==len(arr)-1 or arr[idx+1] > target):
		return True
	return False

def find1st(start, end):

	loc = -1
	while (start <= end):
		mid = (start + end ) // 2
		if arr[mid] > target:
			end = mid - 1
		elif arr[mid] < target:
			start = mid + 1
		else:
			if arr[mid] == target and (mid==0 or arr[mid-1] < target):
				loc = mid
				return loc 
			end = mid - 1

	return loc 

def findlast(start, end):
	loc = -1 
	while start <= end:
		mid = (start + end) // 2
		if arr[mid] > target:
			end = mid - 1
		elif arr[mid] < target:
			start = mid + 1
		else:
			if arr[mid] == target and (mid==len(arr)-1 or arr[mid+1]>target):
				loc = mid 
				return loc
			start = mid + 1
	return loc 

if __name__ == '__main__':
	print( find1st(0, len(arr)-1), findlast(0, len(arr)-1)) 

