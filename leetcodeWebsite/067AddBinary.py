class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a) - 1, len(b) - 1
        carrier = 0
        res = []
        while m >= 0 and n >= 0:
            na, nb = int(a[m]), int(b[n])
            carrier += (na + nb)
            res.append(carrier % 2)
            carrier //= 2

            m -= 1
            n -= 1

        if m >= 0:
            na = int(a[m])
            carrier += na
            res.append(carrier % 2)
            carrier //= 2
            m -= 1

        if n >= 0:
            nb = int(b[n])
            carrier += nb
            res.append(carrier % 2)
            carrier //= 2
            n -= 1

        while carrier:
            res.append(carrier % 2)
            carrier //= 2
        return ''.join(map(str, res[::-1]))

s = Solution()

s.addBinary('1', '111')