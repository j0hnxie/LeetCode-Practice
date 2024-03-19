class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre = 0
        res = 0
        seen = {0: -1}
        for idx, num in enumerate(nums):
            if num == 0:
                pre -= 1
            else:
                pre += 1
            
            if pre in seen:
                res = max(res, idx - seen[pre])
            else:
                seen[pre] = idx
        return res