# 050 幂运算

# 7mins
class Solution:
    def myPow(self, x: float, n: int) -> float:
        symbol = n > 0
        n = n if n > 0 else -n
        if n == 0 and x != 0:
            return 1
        elif n == 1:
            return x if symbol==True else 1./x
        else:
            t = self.myPow(x, n//2)
            t = t * t * (x if n&1 else 1)
            return t if symbol==True else 1. / t

# https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed
Recursive:
class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
Iterative:
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow



# lesson
# if n & 1 was same as: if n % 2
# n >> 1 was same as : n //= 2