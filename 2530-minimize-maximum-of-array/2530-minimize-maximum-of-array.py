class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        prefix = 0
        result = 0

        for idx, num in enumerate(nums):
            prefix += num
            result = max(result, math.ceil(prefix / (idx + 1)))
        
        return result