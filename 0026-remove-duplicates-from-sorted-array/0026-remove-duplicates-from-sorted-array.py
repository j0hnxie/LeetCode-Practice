class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        unique = 1
        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                nums[unique] = nums[i]
                unique += 1
        
        return unique