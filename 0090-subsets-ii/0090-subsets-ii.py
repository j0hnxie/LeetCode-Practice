class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        
        def helper(res, cur, idx):
            if idx == n:
                res.append(list(cur))
                return
            
            num = nums[idx]
            cur.append(num)
            helper(res, cur, idx + 1)
            cur.pop()
            
            while idx < n - 1 and nums[idx] == nums[idx + 1]:
                idx += 1
            
            helper(res, cur, idx + 1)
            
        helper(res, [], 0)
        return res
        
        
        