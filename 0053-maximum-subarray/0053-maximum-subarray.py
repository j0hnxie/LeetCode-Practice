class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dp = []
        
        dp.append(nums[0])
        result = nums[0]
        
        for i in range(1, len(nums)):
            dp.append(nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0))
            result = max(result, dp[i])
        
        return result