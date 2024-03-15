class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        possible = n - 1
        counter = n - 1
        while counter >= 0:
            print(possible)
            if counter + nums[counter] >= possible:
                possible = counter
            counter -= 1
        return possible == 0