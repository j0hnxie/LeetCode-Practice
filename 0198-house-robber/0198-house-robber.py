class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n + 1)]
        dp[1] = nums[0]
        
        for i in range(2, n + 1):
            dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])
        
        print(dp)
        maxCur = dp[0]
        for i in range(n + 1):
            maxCur = max(maxCur, dp[i])
        return maxCur