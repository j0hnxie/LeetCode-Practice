class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max_profit, min_price = 0, float('inf')
        # for price in prices:
        #     min_price = min(min_price, price)
        #     profit = price - min_price
        #     max_profit = max(max_profit, profit)
        # return max_profit
        
        curMax = 0
        overallMax = 0
        diff = list(prices)
        for i in range(1, len(prices)):
            diff[i] = prices[i] - prices[i - 1]
            
        diff[0] = 0
        # print(prices)
        # print(diff)
        
        for i in range(len(diff)):
            curMax += diff[i]
            if curMax < 0:
                curMax = 0
            
            overallMax = max(curMax, overallMax)
        
        return overallMax