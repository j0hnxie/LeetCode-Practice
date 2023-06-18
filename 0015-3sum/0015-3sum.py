class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            low = i + 1
            high = len(nums) - 1
            sumTot = 0
            while low < high:
                sumTot = nums[i] + nums[low] + nums[high]
                if sumTot > 0:
                    high -= 1
                elif sumTot < 0:
                    low += 1
                else:
                    result.append([nums[i], nums[low], nums[high]])
                    last_low = nums[low]
                    last_high = nums[high]
                    while low < high and nums[low] == last_low:
                        low += 1
                    while low < high and nums[high] == last_high:
                        high -= 1
    
        return result