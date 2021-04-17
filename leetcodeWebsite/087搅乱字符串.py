from collections import defaultdict
def h(s1, s2):
    if s1 == s2 or s1 == s2[::-1]:
        return True
    cnter, rcnter, wordcnter = defaultdict(int), defaultdict(int), defaultdict(int)
    i, j = 0, len(s2) - 1
    k = 0
    while i < len(s1):
        cnter[s2[i]] += 1
        rcnter[s2[j]] += 1
        wordcnter[s1[k]] += 1

        if cnter == wordcnter and h(s1[:i + 1], s2[:i + 1]) and h(s1[i + 1:], s2[i + 1:]):
            return True
        if rcnter == wordcnter and h(s1[:i + 1], s2[j:]) and h(s1[i + 1:], s2[:j]):
            return True
        i += 1;
        j -= 1;
        k += 1;
    return False


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return h(s1, s2)
if __name__=="__main__":
    s = Solution()
    s.isScramble("abcde", "caebd")