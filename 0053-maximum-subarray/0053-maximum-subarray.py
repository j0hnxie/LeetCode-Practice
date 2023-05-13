class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        runningTotal = nums[0]
        maxSoFar = nums[0]
        
        for i in range(1, len(nums)):
            runningTotal = max(0, runningTotal) + nums[i]
            maxSoFar = max(maxSoFar, runningTotal)
        
        # print(results)
        return maxSoFar