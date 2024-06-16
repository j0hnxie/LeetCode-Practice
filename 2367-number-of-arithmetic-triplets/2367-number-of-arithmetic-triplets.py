class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # 2 pointer w hashmap
        n, res = len(nums), 0
        last = {}
        l, r = 0, 1
        
        while r < n:
            while nums[r] - nums[l] > diff:
                l += 1
                
            if nums[r] - nums[l] == diff:
                last[r] = last.get(r, 0) + 1
                res += last.get(l, 0)
                
            r += 1
        return res
        
        