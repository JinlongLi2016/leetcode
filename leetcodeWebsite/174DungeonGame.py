from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        f = []
        m, n = len(dungeon), len(dungeon[0])
        for _ in range(m):
            f.append([None] * n)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    f[i][j] = [dungeon[0][0], dungeon[0][0]]
                elif i == 0:
                    energy = f[i][j-1][0] + dungeon[i][j]
                    f[i][j] = [energy, min(f[i][j-1][1], energy)]
                elif j == 0:
                    energy = f[i-1][j][0] + dungeon[i-1][j]
                    f[i][j] = [energy, min(f[i-1][j][1], energy)]
                else:
                    prev = f[i-1][j] if f[i-1][j][1] > f[i][j-1][1] else f[i][j-1]
                    f[i][j] = [prev[0] + dungeon[i][j], min(prev[1], prev[0] + dungeon[i][j])]
        return 1 if f[m-1][n-1][1] >= 0 else 1 - f[m-1][n-1][1]
if __name__=="__main__":
    s = Solution()
    # print(s.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
    print(s.calculateMinimumHP([[-3],[-7]]))