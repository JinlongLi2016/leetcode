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
    
    def func2(self, strs: List[str]) -> str:
        idx = 0
        for t in zip(*strs):
            if len(set(t)) != 1:
                return strs[0][:idx]
            idx += 1
        
        return "" if len(strs)==0 else strs[0][:idx]