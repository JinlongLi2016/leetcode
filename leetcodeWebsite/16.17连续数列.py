# 30mins
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxacc, acc = min(nums), 0
        i = 0
        while i < len(nums):
            if acc <= 0:
                maxacc = max(maxacc, nums[i])
                if nums[i]> 0:
                    acc = nums[i]
            else:
                acc += nums[i]
                maxacc = max(maxacc, acc)
            i += 1

        return maxacc