class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        for idx, n in enumerate(nums):
            if n-1 == idx :
                continue
            else:
                i = nums[idx]
                while 1 <= i <= len(nums) and i != nums[i-1]:
                    t = nums[i-1]
                    nums[i-1] = i
                    i = t
        for idx, n in enumerate(nums):
            if n -1 != idx:
                return idx + 1
        return len(nums) + 1
        
        
# https://leetcode.com/problems/first-missing-positive/discuss/17080/Python-O(1)-space-O(n)-time-solution-with-explanation
 def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
         the range [1,...,l+1] 
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n
    for i in range(1,len(nums)):
        if nums[i]/n==0:
            return i
    return n
    
    
"""
after removing all the numbers greater than or equal to n, all the numbers 
remaining are smaller than n. If any number i appears, we add n to nums[i] 
which makes nums[i]>=n. Therefore, if nums[i]<n, it means i never appears 
in the array and we should return i.
"""


# https://leetcode.com/problems/first-missing-positive/discuss/319270/Explanation-of-crucial-observation-needed-to-deduce-algorithm