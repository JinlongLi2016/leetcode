from functools import reduce

words = ["This", "is", "an", "example", "of", "text", "justification."]
words = ["What","must","be","acknowledgment","shall","be"]
L = 16

if len(words)==0:
	pass
if len(words)==1:
	print(words[0] + ' '* (L - len(words[0])))


i = 0 
j = 0 
l = len(words[0])
final_res = []

while j < len(words):
	l = len(words[i])
	j = i + 1
	while j < len(words) and l + len(words[j]) + 1<=L:
		# 判断j是否可以加入当前行
		l += len(words[j]) + 1
		j += 1
	# 【i，j）
	word_len = 0
	for t in range(i, j):
		word_len += len(words[t])

	left_spaces = L - word_len
	words_num = j - i 
	sep_num = words_num - 1
	if sep_num == 0:
		final_res.append(words[i] + ' ' * left_spaces)
		i = j
		continue
	space_list = [left_spaces//sep_num] * sep_num
	res_space = left_spaces % sep_num
	for t in range(res_space):
		space_list[t] += 1

	# 组装为一行输出
	res = [words[i]]
	for t in range(sep_num):
		res.append(' ' * (space_list[t] if j < len(words) else 1))
		res.append(words[i+1+t])
	if j == len(words):
		res.append(' ' * (left_spaces - words_num + 1))
	final_res.append(''.join(res))
	i = j

print(final_res)