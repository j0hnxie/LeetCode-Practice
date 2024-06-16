class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] - nums[i] > diff:
                    break
                for k in range(j + 1, n):
                    if nums[k] - nums[j] > diff:
                        break
                    if nums[j] - nums[i] == nums[k] - nums[j] == diff:
                        res += 1
        return res