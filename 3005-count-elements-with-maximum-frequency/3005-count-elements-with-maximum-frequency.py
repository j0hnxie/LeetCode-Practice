class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = {}
        maxSoFar = 0
        
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            maxSoFar = max(maxSoFar, counter[num])
        
        res = 0
        for key, value in counter.items():
            if value == maxSoFar:
                res += value
        return res