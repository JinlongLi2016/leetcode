# 14 
def commonPrefix(stra, strb):
    idx = 0
    while len(strb) > idx < len(stra) and stra[idx] == strb[idx]:
        idx += 1
    return stra[:idx]

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        return reduce(commonPrefix, strs, strs[0])