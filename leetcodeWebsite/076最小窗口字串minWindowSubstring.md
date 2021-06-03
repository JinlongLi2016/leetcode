# 076 最小字串窗口

* My Solution: 想法很简单，两个指针i,j，j尽可能地扩展字串，i尽可能地缩减字串长度   

```python
from collections import defaultdict

def isDoneNow(d):
    for k, v in d.items():
        if v > 0:
            return False
    return True
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d, maxd = {}, {}
        d2 = defaultdict(int)
        for c in t:
            if c not in d:
                d[c] = 0
            d[c] += 1
        i = j = 0
        cnt = len(t)
        minStr, minLen = s, len(s)

        while j < len(s):
            while j < len(s) and not isDoneNow(d):  # 有可能两个条件都不满足吗？
                if s[j] in d:
                    d[s[j]] -= 1
                j += 1
            if not isDoneNow(d):
                break
            while i < j and isDoneNow(d):
                if s[i] in d:
                    d[s[i]] += 1
                i += 1
            if j - i + 1 < minLen:
                minLen = j - i + 1
                minStr = s[i - 1: j]

        return minStr

if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
```

考虑s中无包含t的字串情况，它与`if not isDoneNow(d):`的情形一致。算法无法分别这两种情况。因此必要在最开始排除不包含的情况，代码如下：

```python
        for c in s:
            d2[c] += 1
        for k, v in d.items():
            if v > d2[k]:
                return ""
```


* LeetCode Disc: [12 lines Python](https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python)  
The current window is `s[i:j] `and the result window is `s[I:J]`.     
`need[c]` I store how many times I need character c (can be negative) （需要几个字母C）  
`missing` tells how many characters are still missing.


```python
def minWindow(self, s, t):
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1
        if not missing: # missing == 0
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not J or j - i <= J - I:
                I, J = i, j
    return s[I:J]
```



一旦找到一个集合，那么就不存在这missing>0的情况了，

`needs[s[i]] < 0` 表示区间中`s[i]`这个元素过多，以致`needs[s[i]] < 0`，不需要`s[i]`甚至还可以给你一些。



* LeetCode Disc: [Here is a 10-line template that can solve most 'substring' problems](https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems)