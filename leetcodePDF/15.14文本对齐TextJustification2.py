from functools import reduce

'''
1. 判断目前行可以容纳几个单词 [i, j) 
2. 判断单词间应该放几个间隔
3. 输出目前行
'''

words = ["This", "is", "an", "example", "of", "text", "justification."]
# words = ["What","must","be","acknowledgment","shall","be"]
L = 16

if len(words)==0:
	pass
if len(words)==1:
	print(words[0] + ' '* (L - len(words[0])))


i = 0 
l = len(words[0])
final_res = []

while j < len(words):
	l = len(words[i])
	j = i + 1
	while j < len(words) and l + len(words[j]) + 1<=L:
		# 判断j是否可以加入当前行
		l += len(words[j]) + 1
		j += 1
	# [i，j）
	sep_num = j - i - 1
	word_len = l - (j -i - 1)  # j - i - 1

	left_spaces = L - word_len
	words_num = j - i 

	if sep_num == 0:
		final_res.append(words[i] + ' ' * left_spaces)
		i = j
		continue
	# create a 间隔list
	space_list = [left_spaces//sep_num] * sep_num
	res_space = left_spaces % sep_num
	for t in range(res_space):
		space_list[t] += 1

	# 组装为一行输出
	res = [words[i]]
	for t in range(sep_num):
		res.append(' ' * (space_list[t] if j < len(words) else 1)) # 最后一行需要靠左对齐 left justification not fully
		res.append(words[i+1+t])
	
	# 如果为最后一行（靠左对齐，后面还要跟上空格）
	if j == len(words):
		res.append(' ' * (left_spaces - words_num + 1))

	final_res.append(''.join(res))
	i = j

	# 两种特殊情况，只有一个单词和最后一行

print(*final_res)
t = list(map(len, final_res))
# * operator can alse unpack generator
# map(function, iter)
print(final_res, *map(len, final_res))