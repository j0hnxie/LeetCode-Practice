class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numbers = collections.defaultdict(int)

        
        for i in nums:
            numbers[i] += 1
            if numbers[i] > (len(nums) / 2):
                return i