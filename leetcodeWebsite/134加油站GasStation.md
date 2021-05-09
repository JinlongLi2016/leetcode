# 134加油站GasStation

There are `n` gas stations along a circular route, where the amount of gas at the `ith` station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `ith` station to its next `(i + 1)th` station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return *the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return* `-1`. If there exists a solution, it is **guaranteed** to be **unique**

* mine

```python
class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas)
        gain = [gas[i] - cost[i] for i in range(n)]
        s = 0
        while s < n:
            g = 0
            e = s
            flag = False
            while (e != s or (not flag)) and g + gain[e] >= 0:
                g += gain[e]
                e = (e + 1) % n
                flag = True
            if flag and e == s:
                return s
            elif e < s:
                return -1
            else:
                s = e + 1
        return -1
```



* LC 提供了一个更加优雅的解法

```cpp
class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        //determine if we have a solution
        int total = 0;
        for (int i = 0; i < gas.length; i++) {
            total += gas[i] - cost[i];
        }
        if (total < 0) {
            return -1;
        }
   
        // find out where to start
        int tank = 0;
        int start = 0;
        for (int i = 0; i < gas.length;i++) {
            tank += gas[i] - cost[i];
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }
        return start;
    }
}
```

从左往右扫描tank，找到tank搜集为正的初始位置。

* https://leetcode.com/problems/gas-station/discuss/42572/Proof-of-%22if-total-gas-is-greater-than-total-cost-there-is-a-solution%22.-C%2B%2B 证明sum > 0与有解等价