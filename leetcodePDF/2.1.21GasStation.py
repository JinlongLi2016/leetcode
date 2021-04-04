class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        start = -1
        Sum = 0
        total = 0
        i = 0
        while i < len(gas):
        	Sum += gas[i] - cost[i]
        	if Sum < 0:
        		Sum = 0
        		start = i
        	total += gas[i] - cost[i]
        	i += 1
        return start + 1 if total >= 0 else -1



s = Solution()
print(s.canCompleteCircuit([4,5,2,6,5,3], [3,2,7,3,2,9]))