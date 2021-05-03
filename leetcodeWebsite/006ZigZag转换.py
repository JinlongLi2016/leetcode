class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 边界条件
        if numRows == 1:
            return s
        n = (numRows - 1) * len(s) // (2 * numRows - 2) + numRows * 2
        res = []
        for _ in range(numRows):
            res.append([None] * n)

        i, j = 0, 0
        idx = 0
        while idx < len(s):
            while idx < len(s) and i < numRows:
                res[i][j] = s[idx]
                i += 1
                idx += 1
            i -= 2
            j += 1
            while idx < len(s) and i >= 1:
                res[i][j] = s[idx]
                i -= 1
                j += 1
                idx += 1

        pout = []
        for i in range(numRows):
            for j in range(n):
                if res[i][j] is not None:
                    pout.append(res[i][j])
        return ''.join(pout)

if __name__=='__main__':
    s = Solution()
    s.convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.", 4)