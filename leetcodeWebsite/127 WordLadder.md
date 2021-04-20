# 127 WordLadder

A **transformation sequence** from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter.
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`.
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return *the **number of words** in the **shortest transformation sequence** from* `beginWord` *to* `endWord`*, or* `0` *if no such sequence exists.*



* mine: 采用DFS的方式，穷尽搜索。

```python
def isnxtword(x, y):
    return bool(sum([a!=b for a,b in zip(x, y)])==1)

def forward(word, endWord, used, wordList):
    if word == endWord:
        return sum(used) + 1
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
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        used = [False] * len(wordList)
        if endWord not in wordList:
            return 0
        r = forward(beginWord, endWord, used, wordList)
        return r if r != float('inf') else 0
```

对于特定的测试用例，会超时

```
"qa"
"sq"
["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
```



应该注意到的一点是endWord肯定会在跟定的wordList中出现。

为了解决DFS带来的超时问题，可以借鉴迪杰斯特拉算法，构建startWord到每一个word的最短路径，基于此就可以计算出目标。

* 