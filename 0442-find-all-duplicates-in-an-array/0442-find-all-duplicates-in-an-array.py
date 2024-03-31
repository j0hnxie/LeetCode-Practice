class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        
        for idx, num in enumerate(nums):
            if nums[abs(num) - 1] < 0:
                res.append(abs(num))
            
            nums[abs(num) - 1] *= -1
        return res