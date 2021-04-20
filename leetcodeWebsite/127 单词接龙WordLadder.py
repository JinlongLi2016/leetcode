def isnxtword(x, y):
    return bool(sum([a != b for a, b in zip(x, y)])==1)


def forward(word, endWord, used, wordList):
    if word == endWord:
        return sum(used) +1
    if sum(used) == len(wordList):
        return float('inf')
    l = float('inf')
    for idx, (state, d) in enumerate(zip(used, wordList)):
        if not state and isnxtword(word, d):
            used[idx] = True
            l = min(l, forward(d, endWord, used, wordList))
            used[idx] = False
    return l


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        used = [False] * len(wordList)
        if endWord not in wordList:
            return 0
        r = forward(beginWord, endWord, used, wordList)
        print(r)
        return r

if __name__=="__main__":
    s = Solution()
    s.ladderLength("hit",
"cog",
["hot","dot","dog","lot","log","cog"])
    s.ladderLength("qa",
"sq",
["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])