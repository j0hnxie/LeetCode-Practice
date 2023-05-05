class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        left = 0
        right = 1
        maxSoFar = 0
        while right < len(prices):
            cur = prices[right] - prices[left]
            maxSoFar = max(maxSoFar, cur)
            if cur <= 0:
                left = right
            right += 1
            
        return maxSoFar