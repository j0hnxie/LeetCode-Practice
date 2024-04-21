class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        memo1 = [0] * n
        memo2 = [0] * n
        memo1[1] = nums[0]
        memo2[1] = nums[1]
        
        for i in range(2, n):
            memo1[i] = max(memo1[i - 2] + nums[i - 1], memo1[i - 1])
            
        for i in range(2, n):
            memo2[i] = max(memo2[i - 2] + nums[i], memo2[i - 1])
        
        return max(memo1[n - 1], memo2[n - 1])