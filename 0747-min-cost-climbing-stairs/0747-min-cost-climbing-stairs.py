class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = [cost[0], cost[1]]
        n = len(cost)

        for i in range(2, n):
            memo.append(min(memo[i - 1], memo[i - 2]) + cost[i])
        return min(memo[-1], memo[-2])