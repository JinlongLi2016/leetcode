def helper(s, i, p, j):
    if i == len(s) and j == len(p):
        return True

    if (i < len(s) and j >= len(p)) or (i >= len(s) and set(p[j:]) != set(['*'])):
        return False

    if p[j] == '?':
        return helper(s, i + 1, p, j + 1)
    elif p[j] == '*':
        flag = False
        for t in range(i, len(s) + 1):
            flag = helper(s, t, p, j + 1)
            if flag:
                return flag
        return flag
    else:
        if s[i] == p[j]:
            return helper(s, i + 1, p, j + 1)
        else:
            return False


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # i的下一个位置为待放的位置
        i, j = 0, 1
        res = [0] * len(p)
        if len(p) == 0:
            if len(s) == 0:
                return True
            else:
                return False
        res[0] = p[0]
        while j < len(p):
            if res[i] == p[j] == '*':
                j += 1
            else:
                i += 1
                res[i] = p[j]
                j += 1
        res = res[:i + 1]
        return helper(s, 0, ''.join(res), 0)

if __name__=='__main__':
    s = Solution()
    s.isMatch("babab", "?**b*?")