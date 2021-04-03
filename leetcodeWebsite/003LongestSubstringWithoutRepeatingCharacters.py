class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	i, j = 0, 0
    	maxLen = 0
    	wordSet = set()
    	while j < len(s):
    		while s[j] in wordSet:
    			wordSet.remove(s[i])
    			i += 1
    		wordSet.add(s[j])
    		j += 1
    		maxLen = max(0, len(s))
    	return maxLen

# 时间复杂度 O(n) 空间复杂度 O(wordset)