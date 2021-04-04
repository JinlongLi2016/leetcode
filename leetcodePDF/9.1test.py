from collections import namedtuple, deque


def reachable_(aword, bword):
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

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        potentials = wordList + [endWord]
        start = beginWord
        end = endWord

        wordlize = namedtuple('wordlize', ['word', 'length'])


        Q = deque()
        st = wordlize(start, 1)

        Q.append(st)

        while len(Q) > 0:
            tmp= Q.popleft()
            if tmp.word == end:
                return tmp.length
            else:
                for p in potentials:
                    if reachable_(tmp.word, p):
                        Q.append(wordlize(p, tmp.length+1))
                        potentials.remove(p)
        return 0


sol = Solution()
print(sol.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
