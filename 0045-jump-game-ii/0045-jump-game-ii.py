class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        curMax = 0
        curEnd = 0
        
        for i in range(n - 1):
            curJump = nums[i] + i
            curMax = max(curMax, curJump)
            
            if i == curEnd:
                jumps += 1
                curEnd = curMax
        
        return jumps