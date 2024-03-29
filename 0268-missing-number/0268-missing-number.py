class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n + 1) * n / 2
        
        for i in range(n):
            total -= nums[i]
        
        return int(total)