class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n + 1)]
        
        for i in range(1, n + 1):
            cur = nums[i - 1]
            if i >= 3:
                cur += max(dp[i - 2], dp[i - 3])
            dp[i] = cur
        
        print(dp)
        maxCur = dp[0]
        for i in range(n + 1):
            maxCur = max(maxCur, dp[i])
        return maxCur