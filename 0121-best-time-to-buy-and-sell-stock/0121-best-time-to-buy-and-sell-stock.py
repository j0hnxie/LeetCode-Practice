class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxSoFar = 0
        cur = 0
        
        for i in range(1, len(prices)):
            cur = max(0, cur + prices[i] - prices[i - 1])
            maxSoFar = max(cur, maxSoFar)
        
        return maxSoFar