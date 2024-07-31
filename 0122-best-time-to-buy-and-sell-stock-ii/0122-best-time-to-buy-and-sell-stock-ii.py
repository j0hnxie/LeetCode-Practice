class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        bought = [float('-inf')] * n
        sold = [0] * n

        for idx in range(n):
            bought[idx] = max(bought[idx - 1], sold[idx - 1] - prices[idx])
            sold[idx] = max(sold[idx - 1], bought[idx - 1] + prices[idx])

        return max(sold[-1], bought[-1])