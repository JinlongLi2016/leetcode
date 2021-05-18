
* My Solution
```python
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)
        n = len(s)
        res = ''
        ptr = 0
        while ptr < n:
            t = s[ptr]
            cnt = 0
            while ptr < n and s[ptr] == t:
                ptr += 1
                cnt += 1
            res += (str(cnt) + t)
        return res
```

* LeetCode [Disc](https://leetcode.com/problems/count-and-say/discuss/15999/4-5-lines-Python-solutions)
```python
def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    return s
```