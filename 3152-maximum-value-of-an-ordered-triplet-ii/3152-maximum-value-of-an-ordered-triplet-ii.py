class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        result = 0
        largest = max(nums[1], nums[0])
        gap = nums[0] - nums[1]

        for k in range(2, n):
            result = max(result, gap * nums[k])
            gap = max(gap, largest - nums[k])
            largest = max(largest, nums[k])
        
        return result