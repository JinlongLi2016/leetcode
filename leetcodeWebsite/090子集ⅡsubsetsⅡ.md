# 090 子集Ⅱ

Given an integer array `nums` that may contain duplicates, return *all possible subsets (the power set)*.

The solution set **must not** contain duplicate subsets. Return the solution in **any order**.

* My Solution: 回溯法

```python 
import collections
def forward(chars, d, idx, path, res):
    if idx == len(chars):
        res.append(path)
    else:
        for i in range(d[chars[idx]] + 1):
        # for i in [0, d[chars[idx]]]
            forward(chars, d, idx + 1, path + [chars[idx]] * i, res)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        cnter = collections.Counter(nums)
        chars = list(cnter.keys())
        res = []
        forward(chars, cnter, 0, [], res)
        return res
```

* LeetCode Disc: [Simple python solution (DFS)](https://leetcode.com/problems/subsets-ii/discuss/30305/Simple-python-solution-(DFS).)

```python
class Solution(object):
    def subsetsWithDup(self, nums):
        ret = []
        self.dfs(sorted(nums), [], ret)
        return ret
    
    def dfs(self, nums, path, ret):
        ret.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.dfs(nums[i+1:], path+[nums[i]], ret)	
```

深度优先搜索，较难理解。它认为dfs(nums)能够生成nums的所有子集

和`LC077组合`有点类似，`dfs(nums[i+1:], path + [nums[i], ret])` 在调用更深函数的时候，都是抛弃了[0, i]之间的元素

* LeetCode Disc: [Simple python solution without extra space.](https://leetcode.com/problems/subsets-ii/discuss/30166/Simple-python-solution-without-extra-space.)

```python
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
        return res
```

if S[i] is same to S[i - 1], then it needn't to be added to all of the subset, just add it to the last l subsets which are created by adding S[i - 1]

> 对每个新元素，将其加入已生成的子集每个元素中。借此可以将问题规模扩大1.
>
> 如果待新增的元素e已经加过一次了。那么加之前子集可以分为三部分：一部分不包括e，一部分只包括一个e。那么，我们可以通过只包括一个e这一部分来扩大为第三部分，包括两个e的集合。	