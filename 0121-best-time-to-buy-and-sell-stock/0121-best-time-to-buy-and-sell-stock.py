class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        minPrice = prices[0]
        maxSoFar = 0
        for i in prices:
            minPrice = min(minPrice, i)
            cur = i - minPrice
            maxSoFar = max(maxSoFar, cur)
            
        return maxSoFar