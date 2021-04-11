# 067二进制串求和

Given two binary strings `a` and `b`, return *their sum as a binary string*.



* My Solution

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a) - 1, len(b) -1
        carrier = 0
        res = []
        while m >= 0 and n >= 0:
            na, nb = int(a[m]), int(b[n])
            carrier += (na + nb)
            res.append(carrier % 2)
            carrier //= 2
            
            m -= 1
            n -= 1
            
        while m >= 0:
            na = int(a[m])
            carrier += na
            res.append( carrier % 2)
            carrier //= 2
            m -= 1
                
        while n >= 0:
            nb = int(b[n])
            carrier += nb
            res.append( carrier % 2)
            carrier //= 2
            n -= 1
            
        while carrier:
            res.append( carrier % 2)
            carrier //= 2
        return ''.join(map(str, res[::-1]))
```



* LeetCode [Disc](https://leetcode.com/problems/add-binary/discuss/24500/An-accepted-concise-Python-recursive-solution-10-lines)

```python
class Solution:
    def addBinary(self, a, b):
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        else:
            return self.addBinary(a[0:-1],b[0:-1])+'1'
```

