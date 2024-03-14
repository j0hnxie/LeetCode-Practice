class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = 0
        prefixs = {}
        res = 0
        
        for num in nums:
            prefix += num
            if prefix == goal:
                res += 1
            
            comp = prefix - goal
            res += prefixs.get(comp, 0)
            prefixs[prefix] = prefixs.get(prefix, 0) + 1
            # print(res)
            # print(prefixs)
        return res