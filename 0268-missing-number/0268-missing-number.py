class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        
        for num in range(len(nums) + 1):
            res ^= num
        
        return res