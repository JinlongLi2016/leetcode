class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        state = [0] * (n+1)
        state[0] = 1
        for i in range(1, m+1):
            for j in range(n, 0, -1):
                if s[i-1] == t[j-1]:
                    state[j] += state[j-1]
        return state[n]

if __name__=="__main__":
    s = Solution()
    print(s.numDistinct("rabbbit", "rabbit"))