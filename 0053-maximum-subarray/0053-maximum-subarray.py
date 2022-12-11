class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxSum = nums[0]
        curSubarray = 0
        for i in nums:
            curSubarray += i
            if curSubarray > maxSum:
                maxSum = curSubarray
            if curSubarray < 0:
                curSubarray = 0
              
        return maxSum