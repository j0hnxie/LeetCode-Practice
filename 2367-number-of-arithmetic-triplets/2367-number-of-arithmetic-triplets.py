class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # 2 pointer w no hashmap
        n, res = len(nums), 0
        l, m = 0, 1
        
        while m < n:
            while nums[m] - nums[l] > diff:
                l += 1
                
            if nums[m] - nums[l] == diff:
                r = m + 1
                while r < n and nums[r] - nums[m] <= diff:
                    if nums[r] - nums[m] == diff:
                        res += 1
                    r += 1
            
            m += 1
        return res
        
        