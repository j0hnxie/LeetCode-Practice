class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        result = 0
        for num in nums:
            if num > nums[result]:
                result += 1
                
        return result