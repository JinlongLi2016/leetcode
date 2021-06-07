class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        is_pos = (numerator > 0) ^ (denominator > 0)
        numerator, denominator = abs(numerator), abs(denominator)

        q, r = divmod(numerator, denominator)
        res, lst = [], []
        while r:
            if r in lst:
                res.insert(lst.index(r) - len(lst), "(")
                res.append(")")
                break
            lst.append(r)
            res.append(str(r // denominator))
            r = r % denominator
            r *= 10
        print(res)
        res.insert(1, ".")
        if q > 0:
            res[0] = str(q)
        return "".join(res)

if __name__=='__main__':
    s = Solution()
    # print(s.fractionToDecimal(1, 214748364))
    # print(s.fractionToDecimal(1, 2))
    print(s.fractionToDecimal(1, 3))
    # print(s.fractionToDecimal(-1, -2147483648))
    print(s.fractionToDecimal(4, 333))
    print(s.fractionToDecimal(2, 3))
