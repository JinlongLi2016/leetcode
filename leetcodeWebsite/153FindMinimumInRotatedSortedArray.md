# 153FindMinimumInRotatedSortedArray

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times. For example, the array `nums = [0,1,2,4,5,6,7]` might become:

- `[4,5,6,7,0,1,2]` if it was rotated `4` times.
- `[0,1,2,4,5,6,7]` if it was rotated `7` times.

Notice that **rotating** an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array `nums` of **unique** elements, return *the minimum element of this array*.

* mine: 二分法，确定最小值在前半部分还是后半部分，然后将开始或结束游标更新到middle处

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        st, end = 0, len(nums) - 1
        while st < end:
            mid = (st + end) // 2
            if nums[st] < nums[end]:
                return nums[st]
            else:
                if nums[mid] >nums[end]:
                    st = mid + 1
                else:
                    end = mid
        return nums[st]
```



* 同样的方法可以应用到`leetcode-154`，两道题的区别是在154中可以允许元素出现重复值

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        st, end = 0, len(nums) - 1
        while st < end:
            mid = (st + end) // 2
            if nums[st] < nums[end]:
                return nums[st]
            elif nums[st] == nums[end]: # (*) added
                st += 1
            else:
                if nums[mid] >nums[end]:
                    st = mid + 1
                else:
                    end = mid
        return nums[st]
```

所以在代码中，添加了一行来处理相等的情况。

