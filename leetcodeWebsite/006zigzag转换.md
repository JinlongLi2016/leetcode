# 006zigzag转换

* mine

```python
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
                idx +=1 
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
```

空间复杂度为`O(n)`，是否可以降低？

* 稍作提高，降低空间复杂度

```python
from functools import reduce
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 边界条件
        if numRows == 1:
            return s
        res  = []
        for _ in range(numRows):
            res.append([])
        
        i, j = 0, 0
        idx = 0
        while idx < len(s):
            while idx < len(s) and i < numRows:
                res[i] += s[idx],
                i += 1
                idx +=1 
            i -= 2
            while idx < len(s) and i >= 1:
                res[i] += s[idx],
                i -= 1
                idx += 1
        
        pout = reduce(lambda x, y: x+y, res)
        return "".join(pout)
```




* ##### Easy [to understand Java solution](https://leetcode.com/problems/zigzag-conversion/discuss/3403/Easy-to-understand-Java-solution)

```python
public String convert(String s, int nRows) {
    char[] c = s.toCharArray();
    int len = c.length;
    StringBuffer[] sb = new StringBuffer[nRows];
    for (int i = 0; i < sb.length; i++) sb[i] = new StringBuffer();
    
    int i = 0;
    while (i < len) {
        for (int idx = 0; idx < nRows && i < len; idx++) // vertically down
            sb[idx].append(c[i++]);
        for (int idx = nRows-2; idx >= 1 && i < len; idx--) // obliquely up
            sb[idx].append(c[i++]);
    }
    for (int idx = 1; idx < sb.length; idx++)
        sb[0].append(sb[idx]);
    return sb[0].toString();
}
```

