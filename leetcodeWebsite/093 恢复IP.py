def helper(s, n, path, res):
    if s == '' and n == 0:
        res.append('.'.join(path))
    elif s == '' or n == 0:
        return
    else:
        helper(s[1:], n - 1, path + [s[0]], res)
        if s[0] == '0':
            return
        if len(s) > 1:
            helper(s[2:], n - 1, path + [s[:2]], res)
        if len(s) > 2 and 100 <= int(s[:3]) <= 255:
            helper(s[3:], n - 1, path + [s[:3]], res)


class Solution:
    def restoreIpAddresses(self, s: str):
        res = []
        helper(s, 4, [], res)
        return res

if __name__=='__main__':
    s = Solution()
    # s.restoreIpAddressesdresses("25525511135")
    print(s.restoreIpAddresses('1111'))