class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = sorted(list(set(nums)))
        n = len(sort)
    
        res = 0
        counter = 1
        for i in range(1, n):
            res = max(res, counter)
            if sort[i - 1] + 1 == sort[i]:
                counter += 1
            else:
                counter = 1
        
        if n > 0:
            res = max(res, counter)
        return res