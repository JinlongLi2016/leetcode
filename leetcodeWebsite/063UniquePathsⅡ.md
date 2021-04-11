# 063 Unique Paths

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        state = [0] * n
        state[0] = 1 - obstacleGrid[0][0]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    state[j] = 0
                elif j == 0:
                    continue
                elif i == 0:
                    state[j] = state[j-1]
                else:
                    state[j] += state[j-1]
        return state[n-1]
```

边界情况，如果石头放在初始的地方。

