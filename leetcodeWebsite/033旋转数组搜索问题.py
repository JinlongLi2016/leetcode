

# 12mins,主要在调试 target与 [i, m] [m+1, j]边界值大于等于的问题
def bs(nums, i, j, target):
    if i > j or (i==j and nums[i] != target):
        return -1
    m = (i + j) // 2
    if nums[m] == target:
        return m 
    elif nums[i] < nums[m]:
        if nums[i] <= target < nums[m]:
            return bs(nums, i, m-1, target)
        else:
            return bs(nums, m+1, j, target)
    else:
        if nums[m+1] <= target <= nums[j]:
            return bs(nums, m+1, j, target)
        else:
            return bs(nums, i, m-1, target)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bs(nums, 0, len(nums) -1, target)
        
        
* https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple

# 如果nums[m]与 target在nums[0]的同一侧（同时大于nums[0]）,则取nums[m]的值
# 否则则将nums[m]返回的值置为inf/-inf,根据target与nums[0]的关系

int search(vector<int>& nums, int target) {
    int lo = 0, hi = nums.size();
    while (lo < hi) {
        int mid = (lo + hi) / 2;
        
        double num = (nums[mid] < nums[0]) == (target < nums[0])
                   ? nums[mid]
                   : target < nums[0] ? -INFINITY : INFINITY;
                   
        if (num < target)
            lo = mid + 1;
        else if (num > target)
            hi = mid;
        else
            return mid;
    }
    return -1;
}