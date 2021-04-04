
MIN = -2147483648
MAX = 21474837

def atoi(a_string):
	if len(a_string) < 1:
		return 0
	i = 0
	while i < len(a_string):
		if a_string[i] == ' ':
			i += 1
		else:
			break
	if i == len(a_string):
		return 0

	flag = 1
	if a_string[i] == '-':
		flag = -1
		i += 1
	elif a_string[i] == '+':
		falg = 1
		i += 1

	res = 0
	while i < len(a_string):
		if '0' <= a_string[i] <= '9':
			res = res * 10 + int(a_string[i])
		else:
			break 
		i += 1

	if MIN <= res <= MAX:
		return res * flag
	else:
		return 0

if __name__ == '__main__':
	s = '-'
	print(atoi(s))

