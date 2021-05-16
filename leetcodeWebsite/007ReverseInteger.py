class Solution:
    def reverse(self, x: int) -> int:
        isNeg = x < 0
        if isNeg: x = -x
        rerLst = []
        if x == 0:
            rerLst.append(0)
        while x > 0:
            rerLst.append(x % 10)
            x = x // 10
        revLst = rerLst
        r = revLst[0]
        i = 1
        while i < len(revLst):
            r = 10 * r + revLst[i]
            i += 1
        if -2<<32 <= r <= 2<<31 - 1:
            return -r if isNeg else r
        else:
            return 0