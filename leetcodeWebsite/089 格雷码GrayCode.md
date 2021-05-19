# 089 格雷码GrayCode

The gray code is a binary numeral system where two successive values differ in **only one bit**.

Given an integer `n` representing the total number of bits in the code, return **any** sequence of gray code.

A gray code sequence must begin with `0`.



* Mine: 想法很简单，基于n位的格雷码构建n+1位的格雷码。

```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        ret = self.grayCode(n-1)
        ret = [r<<1 for r in ret] + [(r<<1) + 1 for r in ret[::-1]]
        return ret
```

将n位格雷码的顺序reverse过来，再和原样拼接起来就可以构成一个规模为原样2倍的n+1位格雷码

* LeetCode pdf 提供了一个从自然数`i`到其格雷码的数学公式，可以很方便的计算。$graycode(n) = n ⊕ (n/2)  $



注重方法？

我们有一个小刀，要削一个菠萝。怎么做？可以把菠萝的每个坑来挖一刀，亦或是一圈一圈把这些坑都移除掉，后者就是一个方法，有效率。