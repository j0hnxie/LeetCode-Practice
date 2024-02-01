class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        
        for i in range(0, n, 3):
            diffOne = nums[i + 1] - nums[i]
            diffTwo = nums[i + 2] - nums[i + 1]
            diffThree = nums[i + 2] - nums[i]
            
            if diffOne > k or diffTwo > k or diffThree > k:
                return []
            else:
                res.append([nums[i], nums[i + 1], nums[i + 2]])
        return res