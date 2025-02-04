class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        current = 0
        prev = float('inf')
        for num in nums:
            current = num if num <= prev else current + num
            prev = num
            result = max(result, current)

        return result