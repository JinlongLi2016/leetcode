# 072编辑距离

设A和B是2个字符串，要用最少的字符操作将字符串A转换为字符串B。这里所说的字符操作包括：

       (1)删除一个字符(delete)；
    
       (2)插入一个字符(insert)；
    
       (3)将一个字符改为另一个字符(substitute)。

* M1: 动态方程


$$
dp[i][j] = min(dp[i - 1][j - 1] , dp[i][j - 1] , dp[i - 1][j] ) + 1, if A[i] != B[j]     
$$

$$
dp[i][j] = dp[i - 1][j - 1], if A[i] == B[j]
$$




```python
from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None) # no cache method will raise `time limit exceeded`
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m == 0 or n == 0:
            return max(m, n)
        return min(min(self.minDistance(word1[:m-1], word2), 
                  self.minDistance(word1, word2[:n-1])) + 1, 
                   self.minDistance(word1[:m-1], word2[:n-1]) + int(word1[m-1]!=word2[n-1]))
    def minDistance2(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        f = []
        for _ in range(m+1):
            f.append([0] * (n+1))
        for i in range(m+1):
            for j in range(n+1):
                if i == 0:
                    f[i][j] = j
                elif j == 0:
                    f[i][j] = i
                else:
                    d = 1 if word1[i-1] != word2[j-1] else 0
                    f[i][j] = min(f[i][j-1] + 1, 
                                 f[i-1][j] + 1,
                                 f[i-1][j-1] + d)
        return f[m][n]
```



This [link](https://leetcode.com/problems/edit-distance/discuss/25846/C++-O(n)-space-DP) provides a nice `one-row` dynamic method. And [this](https://leetcode.com/problems/edit-distance/discuss/25846/C++-O(n)-space-DP/24822) demonstrates its running process.

































- 转换[方程](https://www.jianshu.com/p/a617d20162cf)



![](https://upload-images.jianshu.io/upload_images/244848-e66264ce2243ddfb.png?imageMogr2/auto-orient/strip|imageView2/2/w/1058/format/webp)