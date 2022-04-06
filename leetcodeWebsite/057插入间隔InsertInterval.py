# 057 插入间隔


# MySolution: 13mins， 核心思想是插入到该列表中，再采用合并间隔的方案对间隔进行合并
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx = 0
        while idx < len(intervals):
            i = intervals[idx]
            if i[0] >= newInterval[0]:
                break
            idx += 1

        intervals.insert(idx, newInterval)
        res = []
        for i in intervals:
            if res and res[-1][1] >= i[0]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res += i,
        return res


# https://leetcode.com/problems/insert-interval/discuss/21622/7%2B-lines-3-easy-solutions
def insert(self, intervals, newInterval):
    s, e = newInterval.start, newInterval.end
    left, right = [], []
    for i in intervals:
        if i.end < s:
            left += i,
        elif i.start > e:
            right += i,
        else:
            s = min(s, i.start)
            e = max(e, i.end)
    return left + [Interval(s, e)] + right