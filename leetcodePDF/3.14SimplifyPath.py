# 简化路径
# rare case: /home//project  /../ 

def scanPattern(s, i):
	p = []
	while i < len(s) and  s[i] != '/':
		p.append(s[i])
		i += 1
	return ''.join(p), i

def simplify_path(s):
	i = 0
	stack = []
	if len(s) < 1:
		return '/'
	if s[i] == '/':
		stack.append(s[i])
		i += 1
	while i < len(s):
		p, i = scanPattern(s, i)
		if p == '' or p == '.':
			i += 1
		elif p == '..':
			stack.pop()
			while len(stack) > 0 and stack[-1] != '/':
				stack.pop()
			if len(stack) == 0:
				stack.append('/')
			i += 1
		else:
			stack.append(p)
			stack.append('/')
			i += 1
	if len(stack) > 1:
		stack.pop()
	print(stack)

simplify_path("/a/./b/../../c/")
simplify_path('/../')
simplify_path('/home//foo/../')

