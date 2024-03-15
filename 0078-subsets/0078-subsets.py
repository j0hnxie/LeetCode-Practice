class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]]
        
        def backtracking(cur, index):
            if index == n:
                return

            backtracking(cur, index + 1)
            cur.append(nums[index])
            res.append(cur.copy())
            backtracking(cur, index + 1)
            cur.pop()
            
        backtracking([], 0)
        return res
        