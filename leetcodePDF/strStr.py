# 3.2 Implement strStr()

def strStr(hayjack, needle):
	if len(needle) < 1:
		return -1

	for i in range(0, len(hayjack) - len(needle)):
		j = i 
		k = 0
		while j < len(hayjack) and k < len(needle) \
			and hayjack[j] == needle[k]:
			j += 1
			k += 1
		if k == len(needle):
			return i 
	return -1

if __name__ == '__main__':
	hayjack = 'helloworld'
	needle = 'low'
	print(strStr(hayjack, needle))