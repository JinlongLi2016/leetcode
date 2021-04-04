#coding:utf-8
s = 'abcabcabc'

from collections import defaultdict
d = defaultdict(int)

# initial state
l = 0
d[s[0]] = 1
max_len = 0


#
for i, c in enumerate(s[1:], start = 1):
	if d[c] <= 0:	# 如果字符没有出现，就记录这个字符再往后移一位
		d[c] = 1
	else: 	# d[c] > 0，出现字符，就记录此刻区间内有多少字符；再移动区间左侧边界直到把这个字符移除。不改变状态字典dict
		max_len = max(max_len, i - l)
		while l < i and s[l] != c:
			l += 1
		l += 1


print(max_len)