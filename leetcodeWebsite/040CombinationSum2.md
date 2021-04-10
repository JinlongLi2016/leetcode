


```python
def forward(d, s, t, p, res):
    if s == t:
        res.append(p[:])
    elif s > t:
        return 
    else:
        for k, v in d.items():
            for i in range(v+1):
                if s + k*i > t:
                    break
                d[v] -= i
                forward(d, s + k*i, t, p + [k] * i, res)
                d[v] += i

        
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # converting into defaultdict
        d = {}
        for c in candidates:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        res = []
        forward(d, 0, target, [], res)
        return res
```

msg as following:  
```
RecursionError: maximum recursion depth exceeded in comparison
    if s == t:
Line 2 in forward (Solution.py)
  [Previous line repeated 996 more times]
    forward(d, s + k*i, t, p + [k] * i, res)
Line 12 in forward (Solution.py)
    forward(d, s + k*i, t, p + [k] * i, res)
Line 12 in forward (Solution.py)
    forward(d, s + k*i, t, p + [k] * i, res)
Line 12 in forward (Solution.py)
```
使用dict的这种方式似乎永远无法达到终止条件

---

```python
def forward(cands, idx, d, s, t, p, res):
    if s == t:
        res.append(p[:])
    elif s > t or idx >= len(cands):
        return 
    else:
        v = d[cands[idx]]
        
        for i in range(v+1):
            if s + cands[idx] * i > t:
                break
            d[cands[idx]] -= i
            forward(cands,idx+1, d, s + cands[idx] * i, t, p + [cands[idx]] * i, res)
            d[cands[idx]] += i

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # converting into defaultdict
        d = {}
        for c in candidates:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        res = []
        forward(candidates, 0, d, 0, target, [], res)
        return res
```
函数似乎会将所有的答案复制为两份呢
```
Your input
[10,1,2,7,6,1,5]
8
Output
[[6,1,1],[7,1],[2,1,5],[2,6],[1,6,1],[1,7],[1,2,5],[1,1,6]]
Expected
[[1,1,6],[1,2,5],[1,7],[2,6]]
```
这里candidates不能够作为衡量进度的标尺，而应该以candidates的set

* My Final Solution 
```python
def forward(cands, idx, d, s, t, p, res):
    if s == t:
        res.append(p[:])
    elif s > t or idx >= len(cands):
        return
    else:
        v = d[cands[idx]]

        for i in range(v + 1):
            if s + cands[idx] * i > t:
                break
            d[cands[idx]] -= i
            forward(cands, idx + 1, d, s + cands[idx] * i, t, p + [cands[idx]] * i, res)
            d[cands[idx]] += i

class Solution:
    def combinationSum2(self, candidates, target):
        # converting into defaultdict
        d = {}
        for c in candidates:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        res = []
        cands = list(set(d.keys()))
        forward(cands, 0, d, 0, target, [], res)
        return res
```


* LeetCode [Disc](https://leetcode.com/problems/combination-sum-ii/discuss/16944/Beating-98-Python-solution-using-recursion-with-comments)

```python 
def combinationSum2(self, candidates, target):
    # Sorting is really helpful, se we can avoid over counting easily
    candidates.sort()                      
    result = []
    self.combine_sum_2(candidates, 0, [], result, target)
    return result
    
def combine_sum_2(self, nums, start, path, result, target):
    # Base case: if the sum of the path satisfies the target, we will consider 
    # it as a solution, and stop there
    if not target:
        result.append(path)
        return
    
    for i in xrange(start, len(nums)):
        # Very important here! We don't use `i > 0` because we always want 
        # to count the first element in this recursive step even if it is the same 
        # as one before. To avoid overcounting, we just ignore the duplicates
        # after the first element.
        if i > start and nums[i] == nums[i - 1]:
            continue

        # If the current element is bigger than the assigned target, there is 
        # no need to keep searching, since all the numbers are positive
        if nums[i] > target:
            break

        # We change the start to `i + 1` because one element only could
        # be used once
        self.combine_sum_2(nums, i + 1, path + [nums[i]], 
                           result, target - nums[i])
```

这里combine_sum_2()用于计算所有nums从start开始总和等于target的组合（每次将一个元素加入到path中）。`nums[i] == nums[i-1]`的原因是用于防止重复计算？