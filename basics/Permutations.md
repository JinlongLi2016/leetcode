## 排列

一个n个元素的数组，生成其所有的排列。



---

题目没有说都唯一、数组为空。

* 把所有的unique number放在i这个位置。

```python
from collections import Counter
def permutations(nums):
    def btrack(path, i, d, res):
        if i == n:
            res.append(path[:])
        else:
            for k, v in d.items():
				if v > 0:
                    path[i] = k
                    d[k] -= 1
                    btrack(path, i+1, d, res)
                    d[k] += 1
                    
    nums.sort()
    n = len(nums)
               
    ans = []
    btrack([0] * n, 0, Counter(nums), ans)
    return ans
```

