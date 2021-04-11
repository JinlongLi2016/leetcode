def mul(n):
    res = 1
    while n:
        res *= n
        n -= 1
    return res

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        content = list(range(1, n + 1))
        res = []
        k -= 1
        while content:
            unit = mul(n - 1) if n > 1 else 1
            res.append(content.pop(k // unit))
            n -= 1
            k %= unit
        return (''.join(map(str, res)))
