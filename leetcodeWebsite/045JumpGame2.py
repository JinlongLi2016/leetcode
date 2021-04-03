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