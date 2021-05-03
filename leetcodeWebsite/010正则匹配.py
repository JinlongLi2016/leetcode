def helper(s, i, p, j):
    if i >= len(s) and j >= len(p):
        return True

    if i < len(s) and j >= len(p):
        return False
    if i >= len(s) and (j < len(p) and set(p[j + 1:]) != set('*')):
        return False

    if j + 1 < len(p) and p[j + 1] == '*':
        flag = helper(s, i, p, j + 2)
        if flag: return flag

        for t in range(i, len(s) + 1):
            if p[j] == '.' or p[j] == s[t]:
                flag = helper(s, t + 1, p, j + 2)
                if flag: return flag
            else:
                break
        return flag

    if p[j] == '.':
        return helper(s, i + 1, p, j + 1)
    else:
        if s[i] == p[j]:
            return helper(s, i + 1, p, j + 1)
        return False


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return helper(s, 0, p, 0)