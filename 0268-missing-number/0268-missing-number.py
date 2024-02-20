class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        unique = set()
        n = len(nums)
        for i in range(n + 1):
            unique.add(i)
        
        for num in nums:
            unique.remove(num)
        
        for res in unique:
            return res