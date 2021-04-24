class Solution:
    def maxProfitHelper(self, prices):
        state = list(range(len(prices)))
        m = len(prices)
        if m == 1:
            return 0, 0, 0
        leftH = m - 1
        for i in range(m - 1, -1, -1):
            if prices[i] > prices[leftH]:
                leftH = i
            state[i] = leftH
        maxProfit = 0
        maxProfit, _in, _out = 0, 0, 0
        for i in range(m):
            if prices[state[i]] - prices[i] > maxProfit:
                maxProfit = prices[state[i]] - prices[i]
                _in, _out = i, state[i]
        return maxProfit, _in, _out

    def maxProfit(self, prices):
        m = len(prices)
        leftProfit, leftIn, LeftOut = self.maxProfitHelper(prices[:2])
        rightProfit, rightIn, rightOut = self.maxProfitHelper(prices[1:])
        rightOut, rightIn = rightOut + 1, rightIn + 1
        maxP = leftProfit + rightProfit

        for i in range(2, m):
            leftProfit, leftIn, LeftOut = self.maxProfitHelper(prices[:i + 1])
            if i > rightIn:
                rightProfit, rightIn, rightOut = self.maxProfitHelper(prices[i:])
                rightOut, rightIn = rightOut + i, rightIn + i

            maxP = max(maxP, leftProfit + rightProfit)
        return maxP

if __name__=="__main__":
    s = Solution()
    print(s.maxProfit([2,1,4,5,2,9,7]))