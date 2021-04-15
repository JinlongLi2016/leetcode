# 091 解析数量 Decode Ways

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        f = [0] * len(s)
        if len(s) == 0 or int(s[0]) == 0:
            return 0
        f[0] = 1
        for idx, c in enumerate(s[1:], start=1):
            if 0 < int(c) < 10:
                f[idx] = f[idx-1]
                if 10 < int(s[idx-1:idx+1]) <= 26:
                    if idx < 2:
                        f[idx] += 1
                    else:
                        f[idx] += f[idx-2]
            else:
                if s[idx-1] not in ['1', '2']:
                    return 0
                else:
                    if idx < 2:
                        f[idx] += 1
                    else:
                        f[idx] += f[idx-2]
        return f[-1]
```

这里面有一个复杂的判断:`if idx < 2:`

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        f = [1] * (len(s) + 1)
        if len(s) == 0 or int(s[0]) == 0:
            return 0
        for idx, c in enumerate(s, start=1):
            if 0 < int(c) < 10:
                f[idx] = f[idx-1]
                if idx 10 < int(s[idx-2:idx]) <= 26:
                    f[idx] += f[idx-2]
            else:
                if s[idx-1] not in ['1', '2']:
                    return 0
                else:
                    f[idx] = f[idx-2]
        return f[-1]
```





```python
class Solution:
    def numDecodings(self, s: str) -> int:
        f = [1] * (len(s) + 1)
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
        return f[-1]
```

Refine for better

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        f = [1] * (len(s) + 1)
        if len(s) == 0 or int(s[0]) == 0:
            return 0
        for idx, c in enumerate(s, start=1):
            f[idx] = 0
            if 0 < int(c) < 10:
                f[idx] += f[idx-1]
            if s[idx-2:idx] and 10 <= int(s[idx-2:idx]) <= 26:
                f[idx] += f[idx-2]
        return f[-1]
```

* ##### Python: Easy to understand explanation, [bottom up dynamic programming](https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming)

```python
def numDecodings(s): 
	if not s:
		return 0

	dp = [0 for x in range(len(s) + 1)] 
	
	# base case initialization
	dp[0] = 1 
	dp[1] = 0 if s[0] == "0" else 1   #(1)

	for i in range(2, len(s) + 1): 
		# One step jump
		if 0 < int(s[i-1:i]) <= 9:    #(2)
			dp[i] += dp[i - 1]
		# Two step jump
		if 10 <= int(s[i-2:i]) <= 26: #(3)
			dp[i] += dp[i - 2]
	return dp[len(s)]
```

