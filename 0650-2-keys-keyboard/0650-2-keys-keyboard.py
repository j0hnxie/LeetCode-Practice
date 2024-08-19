class Solution:
    def minSteps(self, n: int) -> int:
        memo = [0] * (n + 1)

        for times in range(1, n + 1):
            for factor in range(2, times + 1):
                if times % factor == 0:
                    memo[times] = memo[times // factor] + factor
                    break
        
        return memo[-1]
