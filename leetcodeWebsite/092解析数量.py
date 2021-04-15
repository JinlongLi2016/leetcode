class Solution:
    def numDecodings(self, s: str) -> int:
        f = [1] * (len(s) + 1)
        print("hed")
        if len(s) == 0 or int(s[0]) == 0:
            return 0
        for idx, c in enumerate(s, start=1):
            if 0 < int(c) < 10:
                f[idx] = f[idx-1]
                if s[idx-2:idx] and 10 < int(s[idx-2:idx]) <= 26:
                    f[idx] += f[idx-2]
            else:
                if s[idx-2] not in ['1', '2']:
                    return 0
                else:
                    f[idx] = f[idx-2]
        print(f)
        print("he")
        return f[-1]

if __name__=="__main__":
    s = Solution()
    print(s.numDecodings("10"))