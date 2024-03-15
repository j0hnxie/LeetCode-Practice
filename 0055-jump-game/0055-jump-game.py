class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        possible = [False for i in range(n)]
        possible[0] = True
        
        maxJump = nums[0]
        counter = 0
        while counter <= maxJump and counter < n:
            possible[counter] = True
            maxJump = max(maxJump, counter + nums[counter])
            counter += 1
        # print(possible)
        return possible[n - 1]