class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        numbers = collections.defaultdict(int)

        
        for i in nums:
            numbers[i] += 1
            
        result = 0
        resultTracker = 0
        for keys, values in numbers.items():
            if values > result:
                result = values
                resultTracker = keys
            
        return resultTracker