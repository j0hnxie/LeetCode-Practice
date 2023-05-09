class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        counts = {}
        n = len(nums)
        n /= 2
        for i in nums:
            print(i)
            cur = counts.get(i, 0)
            counts[i] = cur + 1
            if cur + 1 > n:
                return i
            
        