
# 题目描述：

# 环形路上有n个加油站，第i个加油站的汽油量是gas[i].

# 你有一辆车，车的油箱可以无限装汽油。从加油站i走到下一个加油站（i+1）花费的油量是cost[i]，你从一个加油站出发，刚开始的时候油箱里面没有汽油。

# 求从哪个加油站出发可以在环形路上走一圈。返回加油站的下标，如果没有答案的话返回-1。

# 注意：

# 答案保证唯一。


class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas)
        for i in range(len(gas)):
            if gas[i] - cost[i] >= 0:
                break
        t = i
        acc = 0
        i = (i - 1 + n) % n
        while i!=t and gas[i] - cost[i] >=0:
            acc += gas[i] - cost[i]
            i = (i - 1 + n) % n
        if i == t:
            return i
        else:
            end = (i+1) % n
            acc += gas[end] - cost[end]
            i = (end + 1) % n
            while i % n != end and acc + gas[i] - cost[i] >= 0:
                acc += gas[i] - cost[i]
                i = (i+1)%n

            if i == end:
                return end
            else:
                return -1



if __name__ == '__main__':
    # gas, cost = [1,2,3,4,5], [3,4,5,1,2]
    # gas, cost = [2,3,4], [3,4,3]
    gas, cost = [5, 8, 2, 8], [6, 5, 6, 6]
    s = Solution()

    print(s.canCompleteCircuit(gas, cost))