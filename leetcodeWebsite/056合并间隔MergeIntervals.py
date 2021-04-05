
* My Solution
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0])
        if len(intervals) < 2:
            return intervals
        res = [intervals[0]]
        for i in intervals[1:]:
            if res[-1][1] >= i[0]:
                # merge them
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        return res
            

* Can Be Improved
			
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a: a[0])
        if len(intervals) < 2:
            return intervals
        res = []
        for i in intervals:
            if res and res[-1][1] >= i[0]:
                # merge them
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
        return res
            
# https://leetcode.com/problems/merge-intervals/discuss/21227/7-lines-easy-Python
# gives some hint on 'list+=' and 'list.append': += faster, 
# ',' 的作用