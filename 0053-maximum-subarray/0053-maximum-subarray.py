class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        runningTotal = nums[0]
        results = [nums[0]]
        
        for i in range(1, len(nums)):
            runningTotal = max(0 + nums[i], runningTotal + nums[i])
            results.append(max(results[i - 1], runningTotal))
        
        print(results)
        return results[len(nums) - 1]