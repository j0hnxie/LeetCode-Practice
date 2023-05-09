class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        dp = []
        dp.append(0)
        dp.append(1)
        dp.append(2)
        
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        
        return dp[n]