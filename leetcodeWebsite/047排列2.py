ans = [[0,0,0,1,9],[0,0,0,9,1],[0,0,1,0,9],[0,0,1,9,0],[0,0,9,0,1],[0,0,9,1,0],[0,1,0,0,9],[0,1,0,9,0],[0,1,9,0,0],[0,9,0,0,1],[0,9,0,1,0],[0,9,1,0,0],[1,0,0,0,9],[1,0,0,9,0],[1,0,9,0,0],[1,9,0,0,0],[9,0,0,0,1],[9,0,0,1,0],[9,0,1,0,0],[9,1,0,0,0]]
ans.sort()
class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        self.permute_helper(nums, 0, res)
        return res

    def permute_helper(self, nums, start, result):
        if start >= len(nums)-1:
            result.append(nums[:])
        else:
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                nums[start], nums[i] = nums[i], nums[start]
                self.permute_helper(nums, start + 1, result)
                nums[start], nums[i] = nums[i], nums[start]

# s = Solution()
# res = s.permuteUnique([0,1,0,0, 9])
# res.sort()
# print(len(res), res)
# print(len(ans), ans)
# print(res==ans)
s = Solution()
res = s.permuteUnique([0,0, 0,1, 9])
print(len(res), res)