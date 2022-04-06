from typing import List
# 23mins
class Solution:
    def jump(self, nums: List[int]) -> int:
        f = [0] * len(nums)
        i = j = 0
        n = len(nums)
        f[0] = 0
        
        while i < n:
            if i + nums[i] > j:
                while j+1 < n and j < i + nums[i]:
                    f[j+1] = f[i] + 1 
                    j += 1
            i += 1
        return f[n-1]

s = Solution()
s.jump([2, 3, 1, 1, 4])


def jump(nums):
    steps = curEnd = curFarthes = 0
    n = len(nums)
    for i in range(n-1):
        curFarthes = max(curFarthes, i + nums[i])
        if i == curEnd:
            steps += 1
            curEnd = curFarthes
    return steps