# 043 Multiply Strings

# 15.35 - 15.52, 17mins,误做成是'+'
```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            num1, num2 = num2, num1 
        res = 0
        for i, a in enumerate(num1[::-1]):
            for j, b in enumerate(num2[::-1]):
                val1, val2 = int(a), int(b)
                res += (val1 * 10**i) * (val2 * 10**j)
        if res == 0:
            return '0'
        ret = []
        while res > 0:
            ret.append(res%10)
            res = res // 10
        return ''.join([str(e) for e in ret[::-1]])
```



* LeetCode [Discussion](https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation)
  

Start from right to left, perform multiplication on every pair of digits, and add them together. Let's draw the process! From the following draft, we can immediately conclude:

```
 `num1[i] * num2[j]` will be placed at indices `[i + j`, `i + j + 1]` 
```

------



[![Multiplication](https://drscdn.500px.org/photo/130178585/m%3D2048/300d71f784f679d5e70fadda8ad7d68f)](https://drscdn.500px.org/photo/130178585/m%3D2048/300d71f784f679d5e70fadda8ad7d68f)

```java
public String multiply(String num1, String num2) {
    int m = num1.length(), n = num2.length();
    int[] pos = new int[m + n];
   
    for(int i = m - 1; i >= 0; i--) {
        for(int j = n - 1; j >= 0; j--) {
            int mul = (num1.charAt(i) - '0') * (num2.charAt(j) - '0'); 
            int p1 = i + j, p2 = i + j + 1;
            int sum = mul + pos[p2];

            pos[p1] += sum / 10;
            pos[p2] = (sum) % 10;
        }
    }  
    
    StringBuilder sb = new StringBuilder();
    for(int p : pos) if(!(sb.length() == 0 && p == 0)) sb.append(p);
    return sb.length() == 0 ? "0" : sb.toString();
}
```