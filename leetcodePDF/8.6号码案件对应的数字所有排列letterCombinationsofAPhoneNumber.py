

d = {
	'2' : 'abc',
	'3' : 'def',
	'4' : 'ghi',
	'5' : 'jkl',
	'6' : 'mno',
	'7' : 'pqrs',
	'8' : 'tuv',
	'9' : 'wxyz'
}

def func(s, i, l):
	if i == len(s): # 寻找到一个组合
		print(''.join(l))
		return
	for e in d[s[i]]:
		l.append(e)
		func(s, i+1, l)
		l.pop()

if __name__ == '__main__':
	s = '23456789'
	func(s, 0, [])
