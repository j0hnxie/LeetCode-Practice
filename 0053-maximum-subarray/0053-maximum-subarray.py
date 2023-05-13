class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        runningTotal = float('-inf')
        maxSoFar = float('-inf')
        
        for i in nums:
            runningTotal = max(i, runningTotal + i)
            maxSoFar = max(maxSoFar, runningTotal)
        
        # print(results)
        return maxSoFar