# Valid Parenthese

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"(": ")", "{": "}", "[": "]"}
        for c in s:
            if c in d:  stack.append(c)
            elif len(stack) > 0 and d[stack[-1]] == c:
                stack.pop(-1)
            else:
                return False
        return len(stack) == 0
            