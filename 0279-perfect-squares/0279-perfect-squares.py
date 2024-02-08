class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for i in range(n + 1)]
        dp[0] = 0
        # perfectSquares = []
        # counter = 1
        # while counter * counter <= n:
        #     perfectSquares.append(counter * counter)
        #     # dp[counter * counter] = 0
        #     counter += 1
        
        for i in range(1, n + 1):
            # print(dp)
            # for j in perfectSquares:
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        # print(dp)
        return dp[n]