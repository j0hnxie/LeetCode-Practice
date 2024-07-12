class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        n = len(nums)
        rem = set(nums)
        
        def helper(res, cur, rem):
            if len(cur) == n:
                res.append(cur.copy())
                return
            
            for num in rem:
                rem.discard(num)
                cur.append(num)
                helper(res, cur, rem.copy())
                cur.pop()
                rem.add(num)
                
        helper(res, cur, rem)
        return res
        