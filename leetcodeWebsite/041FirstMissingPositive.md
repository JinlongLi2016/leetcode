# 041FirstMissingPositive

Given an unsorted integer array `nums`, find the smallest missing positive integer.

You must implement an algorithm that runs in `O(n)` time and uses constant extra space.

* M1

```python
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
```

* LeetCode： 值`A[i]`与其应该处于的位置`A[i]-1`上的值不等时，应该将`A[i]`归位

```C++
class Solution
{
public:
    int firstMissingPositive(int A[], int n)
    {
        for(int i = 0; i < n; ++ i)
            while(A[i] > 0 && A[i] <= n && A[A[i] - 1] != A[i])//值A[i]与其应该处于的位置A[i]-1上的值不等时，应该将A[i]归位
                swap(A[i], A[A[i] - 1]);
        
        for(int i = 0; i < n; ++ i)
            if(A[i] != i + 1)
                return i + 1;
        
        return n + 1;
    }
};
```

