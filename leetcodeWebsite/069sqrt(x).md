# 069 求根

Given a non-negative integer `x`, compute and return *the square root of* `x`.

Since the return type is an integer, the decimal digits are **truncated**, and only **the integer part** of the result is returned.

* My Solution: binary search

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while not (l * l <= x and (l+1) * (l+1) > x): # l is not what I want
            m = (l + r) // 2
            if m * m <= x:
                l = m
            else:
                r = m
        return l

```



* *LeeCode [Disc](https://leetcode.com/problems/sqrtx/discuss/25057/3-4-short-lines-Integer-Newton-Every-Language)* mentioned that *Newton's method*

```c++
public int sqrt(int x) {
    if (x == 0)
        return 0;
    int left = 1, right = Integer.MAX_VALUE;
    while (true) {
        int mid = left + (right - left)/2;
        if (mid > x/mid) {
            right = mid - 1;
        } else {
            if (mid + 1 > x/(mid + 1))
                return mid;
            left = mid + 1;
        }
    }
}
```

```python
    r = x
    while r*r > x:
        r = (r + x/r) / 2
    return r
```




