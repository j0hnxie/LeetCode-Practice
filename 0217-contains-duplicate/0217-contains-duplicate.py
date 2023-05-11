class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        exists = set(nums)
        # for i in nums:
        #     exists.add(i)
        return len(nums) != len(exists)