class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res, sequence = [], []
        is_neg = numerator * denominator < 0
        numerator, denominator = abs(numerator), abs(denominator)
        q, r = divmod(numerator, denominator)
        res.append(str(q))
        numerator = r

        if numerator > 0:
            res.append('.')
            numerator *= 10
            sequence += numerator,


        while numerator > 0 and numerator not in sequence[:-1]:
            while numerator < denominator:
                res.append('0')
                numerator *= 10
                sequence += numerator,
            q, r = divmod(numerator, denominator)
            res += str(q)
            numerator = r * 10
            if numerator:
                sequence += numerator,
        if numerator in sequence:
            s, e = sequence.index(numerator), len(sequence)
            res.insert(s - e +1, '(')
            res += ')',
        prefix = '-' if is_neg and denominator > 0 else ''
        return prefix + ''.join(res)

if __name__=='__main__':
    s = Solution()
    print(s.fractionToDecimal(1, 214748364))
    print(s.fractionToDecimal(1, 2))
    print(s.fractionToDecimal(1, 3))
    print(s.fractionToDecimal(-1, -2147483648))
