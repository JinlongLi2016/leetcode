from collections import namedtuple, deque 


def reachable(aword, bword):
	cnt = 0

	if len(aword) != len(bword):
		return False
	for a, b in zip(aword, bword):
		if a != b:
			cnt += 1
	if cnt == 1:
		return True
	else:
		return False

start = 'hit'
end = 'cog'

dictionary = ["hot","dot","dog","lot","log"]

wordlize = namedtuple('wordlize', ['word', 'length'])

potentials = dictionary + [end]  # 

Q = deque()
st = wordlize(start, 1)

Q.append(st)

def ex():
	while len(Q) > 0:
		tmp= Q.popleft()
		if tmp.word == end:
			return tmp.length
		else:
			for p in potentials:
				if reachable(tmp.word, p):
					Q.append(wordlize(p, tmp.length+1))
					potentials.remove(p)
	return 0

print(ex())


# 求最短距离，BFS
# DFS, 需要一个队列来维持遍历状态。列表维护潜在可访问节点。同时每个节点还要有一个距离。
