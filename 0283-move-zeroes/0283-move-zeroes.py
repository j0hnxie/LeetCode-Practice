class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        cur_idx = 0
        for num in nums:
            if num != 0:
                nums[cur_idx] = num
                cur_idx += 1
        
        for idx in range(cur_idx, n):
            nums[idx] = 0