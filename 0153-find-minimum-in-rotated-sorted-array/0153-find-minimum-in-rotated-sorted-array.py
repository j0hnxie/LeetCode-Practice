class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid
        return min(nums[0], nums[n - 1])