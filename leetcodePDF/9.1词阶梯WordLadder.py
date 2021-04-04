# https://leetcode.com/problems/word-ladder/discuss/296765/BFS-using-Python-3
from collections import namedtuple, deque

def solution(beginWord, endWord, wordList):
	StringWithDistance = namedtuple('StringWithDistance', ['str_cond', 'disntance'])

	q = deque([StringWithDistance(beginWord, 1)])

	wordSet = set(wordList)
	while q:
		cur_str, cur_distance = q.popleft()
		if cur_str == endWord:
			return cur_distance
		for i in range(len(cur_str)):
			for c in string.ascii_lowercase:
				adj_str = cur_str[:i] + c + cur_str[i+1:]
				if adj_str in wordSet:
					wordSet.remove(adj_str)
					q.append(StringWithDistance(adj_str, cur_distance+1))


def wordladder2(beginWord, endWord, wordList):
	# 某个节点有多个前驱的情况 怎么处理？
	StringWithDistance = namedtuple('StringWithDistance', ['prev_str', 'str_cand', 'distance'])
	q = deque([StringWithDistance(None, beginWord, 1)])

	wordSet = set(wordList)

	target_distance = float('+inf')
	target_strs = []
	while q:
		cur_strs, cur_distance = q.popleft()
		for cur_str in cur_strs:
			if cur_distance > target_distance:
				break

			if cur_str == endWord:
				target_distance = cur_distance
				target_strs.append(cur_str)

			# using wordSet to create a dict with values initlized to []

			candidate_previous = dict.fromkeys(wordSet, value=[])
			for i in range(len(cur_str)):
				for c in string.ascii_lowercase:
					adj_str = cur_str[:i]  + c + cur_str[i+1:]
					if adj_str in wordSet:

						#wordSet.remove(adj_str)
						candidate_previous[adj_str].append(adj_str)

						# q.append(StringWithDistance(cur_str, adj_str, cur_distance+1))
			# 迭代完成之后把 potential_cand里面的东西
			for k, v in candidate_previous.items():
				if v:
					q.append(StringWithDistance(v, k, cur_distance+1))

	# 最后再从后往前遍历结果