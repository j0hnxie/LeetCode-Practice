class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        
        res = 0
        for num in nums:
            if num - 1 not in unique:
                new = num + 1
                while new in unique:
                    new += 1
                res = max(new - num, res)
        return res