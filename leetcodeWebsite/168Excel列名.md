# 168Excel列名

Given an integer `columnNumber`, return *its corresponding column title as it appears in an Excel sheet*.

For example:

```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
```

* M1

```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        res = []
        while n > 0:
            res += chr((n-1) % 26 + 1 + 64),
            n = (n-1) // 26
        return ''.join(res[::-1])
```

