class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        f = []
        for _ in range(n):
            f.append([0] * n)
        for i in range(n):
            f[i][i] = 1
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                f[i][j] = max(f[i+1][j], f[i][j-1])
                if s[i] == s[j]:
                    f[i][j] = max(f[i][j], f[i+1][j-1] + 2)
        maxlen = f[0][n-1]
        l = maxlen
        i, j = 0, n-1
        print(f)
        while i<=j:
            if i+1 < n and f[i][j] == f[i+1][j]:
                i += 1
            elif j-1 >= 0 and f[i][j] == f[i][j-1]:
                j -= 1
            elif i+1 < n and j-1 >= 0 and f[i][j] == f[i+1][j-1]+2:
                return s[i:j+1]
            else:
                return s[i]

if __name__=="__main__":
    s = Solution()
    s.longestPalindrome("aacabdkacaa")