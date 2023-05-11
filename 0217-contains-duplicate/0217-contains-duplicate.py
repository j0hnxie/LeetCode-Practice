class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    
        exists = set()
        for i in nums:
            if i in exists:
                return True
            else:
                exists.add(i)
        return False