class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if amount == 0:
            return 0
        
        maxAmnt = coins[-1]
            
        dp = [amount + 1] * (amount + 1)
        for i in range(len(coins)):
            curCoin = coins[i]
            
            if curCoin <= amount:
                dp[curCoin] = 1
            
        for i in range(1, amount + 1):
            for j in coins:
                if i - j > 0:
                    dp[i] = min(dp[i - j] + 1, dp[i])
                    
        if dp[-1] > amount:
            return -1
        else:
            return dp[-1]