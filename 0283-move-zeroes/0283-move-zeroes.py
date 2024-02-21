class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        start = 0
        for num in nums:
            if num != 0:
                nums[start] = num
                start += 1
        
        for i in range(start, n):
            nums[i] = 0
        
            