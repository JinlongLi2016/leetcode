
d = {')':'('}
def longestValidParentheses(s):
	"""用一个栈来存储匹配信息，并保留在匹配过程中的最长长度信息"""
	if len(s) < 1:
		return 0
	stack = []
	i = 0
	stack.append(s[i])
	i += 1

	length = 0
	MaxLen = 0
	while i < len(s):
		if s[i] == ')':
			if stack[-1] == d[s[i]]:
				stack.pop()
				length += 2
			else:
				MaxLen = max(MaxLen, length)
				while len(stack) > 0:	stack.pop()
				stack.append(s[i])
				length = 0
			i += 1
		else:
			stack.append(s[i])
			i += 1
	MaxLen = max(MaxLen, length)
	print(MaxLen)


# another approach, please refer the leetcode.pdf

longestValidParentheses(')((()())')
