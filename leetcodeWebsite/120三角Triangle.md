# 120三角Triangle

Given a `triangle` array, return *the minimum path sum from top to bottom*.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index `i + 1` on the next row.

* mine 

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = triangle[-1][:]
        t = n - 1
        while t > 0:
            for i in range(t):
                f[i] = min(f[i], f[i+1]) + triangle[t-1][i]
            t -= 1
        return f[0]
```

